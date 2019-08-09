from django.db import models

class Users(models.Model):
    nickName = models.CharField(max_length=50, blank=True, null=True)
    avatarUrl = models.CharField(max_length=200, blank=True, null=True)
    country = models.CharField(max_length=20, blank=True, null=True)
    province = models.CharField(max_length=20, blank=True, null=True)
    lanuage = models.CharField(max_length=20, blank=True, null=True)
    city = models.CharField(max_length=20, blank=True, null=True)
    gender = models.IntegerField(null=True)
    openid = models.CharField(max_length=50)
# Create your models here.
