from django.db import models
from accounts.models import User
from django.contrib.auth.models import AnonymousUser
from django.core.urlresolvers import reverse

from eventlog.models import log
# Create your models here.

class Task(models.Model):
    user = models.ForeignKey(User)
    name = models.CharField(max_length=200)
    date_added = models.DateField(auto_now_add=True)
    deadline_date = models.DateField()
    completed = models.BooleanField(default=False)
    description = models.TextField(default='No description for this Task')

    def get_absolute_url(self):
        return reverse ('task', kwargs={'slug': self.id})

    def __unicode__(self):
        return '%s created %s'%(self.user, self.name)

    class Meta:
        ordering = ['-date_added']
