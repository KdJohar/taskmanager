from django.conf.urls import patterns, url

urlpatterns = patterns(
    url(r'^task/$', 'taskapi.views.task_list', name='task_list'),
    url(r'^task/(?P<id>[0-9]+)/$', 'taskapi.views.task_detail', name='task_detail'),

)
