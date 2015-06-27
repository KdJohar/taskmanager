from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings
from taskapi import views
urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'accounts.views.login', name='login'),
    url(r'^register/$', 'accounts.views.register', name='register'),
    url(r'^logout$', 'accounts.views.logout', name='logout'),
    url(r'^dashboard/$', 'tasks.views.dashboard', name='dashboard'),
    url(r'^dashboard/all-tasks/$', 'tasks.views.alltask', name='alltasks'),
    url(r'^dashboard/activites/$', 'tasks.views.allactivities', name='activites'),
    url(r'^dashboard/all-tasks/completed/$', 'tasks.views.taskcomplete', name='completetasks'),
    url(r'^dashboard/all-tasks/pending/$', 'tasks.views.pendingtask', name='pendingtasks'),
    url(r'^dashboard/all-tasks/today/$', 'tasks.views.todaytask', name='todaytask'),
    url(r'^dashboard/all-tasks/(?P<task_id>\d+)/$', 'tasks.views.task', name='task'),
    url(r'^delete/(?P<task_id>\d+)/$', 'tasks.views.deletetask', name='delete'),
    url(r'^complete/(?P<task_id>\d+)/$', 'tasks.views.completetask', name='complete'),
    url(r'^dashboard/create_task/$', 'tasks.views.createtask', name='createtask'),
    url(r'^api/task/$', 'taskapi.views.tasklist', name='task_list'),
    url(r'^api/task/(?P<id>[0-9]+)/$', 'taskapi.views.taskdetail', name='task_detail'),

    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),

    #url(r'^api/', include('taskapi.urls')),

    url(r'^admin/', include(admin.site.urls)),
)
urlpatterns += patterns('', (
    r'^static/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.STATIC_ROOT}
))
urlpatterns += patterns('', (
    r'^media/(?P<path>.*)$',
    'django.views.static.serve',
    {'document_root': settings.MEDIA_ROOT}
))