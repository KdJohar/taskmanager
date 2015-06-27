from django.db import models
from django.contrib.auth.models import AbstractBaseUser, UserManager, PermissionsMixin
# Create your models here.
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(unique=True)
    joined = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)
    username = models.CharField(max_length=50, null=True)
    USERNAME_FIELD = 'email'
    objects = UserManager()

    def __unicode__(self):
        return self.email



