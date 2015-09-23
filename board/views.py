#coding:utf-8

import datetime
import re, urllib

from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse
from django.utils import html
from django.core.cache import cache, caches

from .models import Post
from .forms import ContentImageForm
from utils.passport import passport_required


@passport_required('board')
def index(request, *args, **kwargs):
    tag = kwargs.get('tag')
    if tag:     #过滤tag
        decode_tag = urllib.parse.unquote(tag)
        post_list_all = Post.objects.filter(title__contains=decode_tag).order_by('-pk')
    else:
        post_list_all = Post.objects.order_by('-pk')

    POST_EVERY_PAGE = 20     #每页显示post条数

    #取得要显示的post
    if request.method == 'GET':
        #翻页数
        max_page = int((len(post_list_all)-1) / POST_EVERY_PAGE) + 1
        try:
            current_page = int(request.GET['page'])
        except:
            current_page = 0

        if current_page > max_page:
            current_page = max_page
        elif current_page < 1:
            current_page = 1
        post_list = post_list_all[(current_page-1)*POST_EVERY_PAGE:current_page*POST_EVERY_PAGE]
    else:
        post_list = Post.objects.order_by('-pk')[:POST_EVERY_PAGE]

    #整理每个post的日期,与上条相同的换为1970年1月1日做标记
    #转换文字内容里面的空格和换行
    last_date = datetime.date(1970, 1, 1)
    for post in post_list:
        if post.datetime.date() == last_date:
            post.datetime = post.datetime.replace(year=1970)
        else:
            last_date = post.datetime.date()

        if post.post_type == 'TXT':
            post.contenttext.content = post.contenttext.content.replace(' ', '&nbsp;').replace('\n', '<br />')

    #把每个post的title里面的tag转换成链接
    to_a = lambda tag :\
        '<a href="'+\
        reverse('blog:index',
                args=(urllib.quote(tag.group('tag').encode('utf-8')), ))+\
        '">'+\
        tag.group('tag')+\
        '</a>'  #这个链接里面URL编码了
    for p in post_list:
        p.title = re.sub('#(?P<tag>.+?)#', to_a, p.title)

    context = {'post_list': post_list,
               'current_page': current_page,
               'page_range': range(1, max_page + 1),
               'base_url': request.path,
               'max_page': max_page,
               'now': datetime.datetime.now(),
    }
    return render(request, 'blog/index.html', context)


@passport_required('board')
def loveletter(request):
    return render(request, 'blog/loveletter.html')


@passport_required('board')
def new(request):
    return render(request, 'blog/new.html')


@passport_required('board')
def post(request):
    if request.method == 'POST':
        po = Post(title=html.escape(request.POST['title']),     #存的时候html转义了，方便显示
                  datetime=datetime.datetime.now(),
                  author='XU')
        po.save()
        #上传的啥类型的po
        if request.POST['type'] == "IMG":
            ContentImage(post=po, content=request.FILES['content']).save()
        elif request.POST['type'] == "TXT":
            ContentText(post=po, content=request.POST['content']).save()
        elif request.POST['type'] == "VOI":
            ContentVoice(post=po, content=request.FILES['content']).save()

