from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from schedule.models import Project, Schedule
from datetime import date, datetime
from django.core.urlresolvers import reverse

def index(request):
    project_list = Project.objects.all()
    context = {'project_list': project_list}
    return render(request, 'schedule/index.html', context)

def project(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render(request, 'schedule/project.html', {'project': p})

def manual(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    return render(request, 'schedule/manual.html', {'project': p})

def detail(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    schedule_list = p.schedule_set.all()

    total_minutes = 0
    for schedule in schedule_list:
        total_minutes += schedule.minutes
    
    context = {'schedule_list': schedule_list,
               'total_minutes': total_minutes,
               'project': p,
    }
    return render(request, 'schedule/detail.html', context)

def addproject(request):
    newp = Project(name = request.POST['name'])
    newp.save()
    return HttpResponse(str(reverse('schedule:project', args=(newp.id,))))

def addschedule(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    m = int(request.POST['workHour']) * 60 + int(request.POST['workMinute'])
    c = request.POST['content']

    try:
        d = datetime.strptime(request.POST['date'], "%Y/%m/%d").date()
    except:
        d = date.today()
    
    try:
        s = p.schedule_set.get(date=d)
    except Schedule.DoesNotExist:
        s = Schedule(project=p, minutes=m, date=d, content=c)
        s.save()
        
        return HttpResponseRedirect(reverse('schedule:detail', args=(project_id,)))

    s.minutes += m
    s.content += '\n' + c
    s.save()
    
    return HttpResponseRedirect(reverse('schedule:detail', args=(project_id,)))

def removeproject(request, project_id):
    p = get_object_or_404(Project, pk=project_id)
    p.delete()
    
    return HttpResponseRedirect(reverse('schedule:index'))

def removeschedule(request, schedule_id):
    s = get_object_or_404(Schedule, pk=schedule_id)
    re = reverse('schedule:detail', args=(s.project.id,))
    s.delete()

    return HttpResponseRedirect(re)
