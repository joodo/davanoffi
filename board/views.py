#coding:utf-8

import re

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.core.urlresolvers import reverse, reverse_lazy
from django.core.exceptions import ObjectDoesNotExist
from django.utils import html
from django.utils.decorators import method_decorator
from django.utils.encoding import smart_text
from django.utils.http import urlquote_plus, unquote_plus
from django.views.generic import ListView
from django.views.generic.edit import CreateView, UpdateView

from utils.passport import passport_required
from .models import Post, Tag
from .forms import PostForm, TagForm


class PostListView(ListView):
    paginate_by = 15
    ordering = '-pk'

    def get_context_data(self, **kwargs):
        context = super(PostListView, self).get_context_data(**kwargs)
        for post in context['post_list']:
            #将 title 中的 tag 变为超链接
            post.title = re.sub('#(?P<tag>.+?)#',
                    add_tag_href,
                    post.title)

        return context

    @method_decorator(passport_required('board'))
    def dispatch(self, *args, **kwargs):
        return super(PostListView, self).dispatch(*args, **kwargs)


class PostAll(PostListView):
    template_name = 'board/post_list.html'
    queryset = Post.objects.filter(parent__isnull=True)


class PostInTag(PostListView):
    template_name = 'board/post_in_tag_list.html'

    def get_queryset(self):
        tag_name = unquote_plus(str(self.kwargs['tag']))
        try:
            tag_obj = Tag.objects.get(name=tag_name)
        except ObjectDoesNotExist:
            tag_obj = None
        return Post.objects.filter(tags__in=[tag_obj])

    def get_context_data(self, **kwargs):
        context = super(PostInTag, self).get_context_data(**kwargs)

        tag_name = unquote_plus(str(self.kwargs['tag']))
        try:
            tag_obj = Tag.objects.get(name=tag_name)
        except ObjectDoesNotExist:
            tag_obj = None
        context['tag'] = tag_obj
        return context


class PostCreateView(CreateView):
    form_class = PostForm
    template_name = 'board/post_create.html'
    success_url = reverse_lazy('board:index')

    @method_decorator(passport_required('board'))
    def dispatch(self, *args, **kwargs):
        return super(PostCreateView, self).dispatch(*args, **kwargs)


class PostDetailView(CreateView):
    form_class = PostForm
    template_name = 'board/post_detail.html'
    success_url = '.'

    def get_context_data(self, **kwargs):
        context = super(PostDetailView, self).get_context_data(**kwargs)
        post_id = int(self.kwargs['pk'])
        context['post'] = get_object_or_404(Post, pk=post_id)
        return context

    @method_decorator(passport_required('board'))
    def dispatch(self, *args, **kwargs):
        return super(PostDetailView, self).dispatch(*args, **kwargs)


class TagSettingView(UpdateView):
    model = Tag
    template_name = 'board/tag_update.html'
    form_class = TagForm

    def get_success_url(self):
        print('dddd')
        tag = Tag.objects.get(pk = self.kwargs['pk'])
        return reverse_lazy('board:tag', kwargs={'tag': urlquote_plus(tag.name)})

    @method_decorator(passport_required('board'))
    def dispatch(self, *args, **kwargs):
        return super(TagSettingView, self).dispatch(*args, **kwargs)


def add_tag_href(tag):
    tag = tag.group('tag')
    text = html.escape(tag)
    url = reverse('board:tag', kwargs={'tag': urlquote_plus(tag)})
    tag = '<a href="%s">#%s#</a>' % (url, text)

    return tag
