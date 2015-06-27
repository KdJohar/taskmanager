from django.shortcuts import render_to_response, redirect, get_object_or_404
from django.shortcuts import RequestContext
from django.contrib.auth.decorators import login_required
from models import Task
from forms import TaskCreationForm
from django.core.urlresolvers import reverse
from django.http import HttpResponse
import datetime
from eventlog.models import Log, log

from django.contrib.admin.models import LogEntry, ADDITION
# Create your views here.
today = datetime.date.today()

@login_required
def dashboard(request):
    user = request.user

    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()

    tasks = Task.objects.filter(user=user).order_by('-id')[:10]
    logs = Log.objects.filter(user=user)[:10]
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()
    count = tasks.count()

    return render_to_response('dashboard/dashboard.html', locals(), context_instance = RequestContext(request))

@login_required
def allactivities(request):
    user = request.user

    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()

    tasks = Task.objects.filter(user=user).order_by('-id')[:10]
    logs = Log.objects.filter(user=user)
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()
    count = tasks.count()

    return render_to_response('dashboard/activities.html', locals(), context_instance = RequestContext(request))

@login_required
def alltask(request):
    user = request.user
    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()

    return render_to_response('dashboard/alltask.html', locals(), context_instance = RequestContext(request))

@login_required
def taskcomplete(request):
    user = request.user
    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()

    return render_to_response('dashboard/completed.html', locals(), context_instance = RequestContext(request))
@login_required
def pendingtask(request):
    user = request.user
    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()

    return render_to_response('dashboard/pending.html', locals(), context_instance = RequestContext(request))

@login_required
def todaytask(request):
    user = request.user
    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()

    return render_to_response('dashboard/todaytask.html', locals(), context_instance = RequestContext(request))

@login_required
def task(request, task_id):
    user = request.user
    task_today = Task.objects.filter(user=user).filter(deadline_date=today)
    task_today_count = task_today.count()
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()

    task_now = get_object_or_404(Task, id=task_id)

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()

    return render_to_response('dashboard/task.html', locals(), context_instance = RequestContext(request))





@login_required
def createtask(request):
    user = request.user
    task_today = Task.objects.filter(deadline_date=today)
    task_today_count = task_today.count()
    task_complete = Task.objects.filter(user=user).filter(completed = True).order_by('-id')
    task_complete_count = task_complete.count()
    task_pending = Task.objects.filter(user=user).filter(completed = False).order_by('-id')
    task_pending_count = task_pending.count()

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()

    if request.method == 'GET':
        form = TaskCreationForm()
    else:
        form = TaskCreationForm(request.POST)
        if form.is_valid():
            print 'hello'
            name = form.cleaned_data['name']
            date = form.cleaned_data['date']
            description = form.cleaned_data['description']
            task_object = Task.objects.create(name=name, user=request.user, deadline_date=date, description=description)
            task_object.save()
            log(user=user, action='Task Created', extra={'name': name})
            return redirect(reverse('dashboard'))
    return render_to_response('dashboard/createtask.html', locals(), context_instance = RequestContext(request))




@login_required
def deletetask(request, task_id):
    user = request.user
    task_now = get_object_or_404(Task, id=task_id)

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()
    if task_now.user == user:
        task_now.delete()
        log(user=user, action='Task Deleted', extra={'name': task_now.name})
        return redirect(reverse('dashboard'))
    else:
        return HttpResponse("Task connot be deleted")
@login_required
def completetask(request, task_id):
    user = request.user
    task_now = get_object_or_404(Task, id=task_id)

    tasks = Task.objects.filter(user=user).order_by('-id')
    count = tasks.count()
    if task_now.user == user:
        task_now.completed = True
        task_now.save()
        log(user=user, action='Task Completed', extra={'name': task_now.name})
        return redirect(reverse('dashboard'))
    else:
        return HttpResponse("Task connot be completed")
