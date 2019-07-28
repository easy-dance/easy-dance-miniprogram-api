from django.db import models

class HelloWorld(models.Model):
    who = models.CharField(max_length=20)

class HiThisIsATest(models.Model):
    when = models.CharField(max_length = 20)

# Create your models here.