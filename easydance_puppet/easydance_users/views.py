from django.shortcuts import render
from django.http import HttpResponse
from . import models
import json


def login(req):
  print('Login!')
  dic = {'username': req.GET.get('username'), 'password': req.GET.get('password')}
  users = models.Users(**dic)
  users.save()
  return HttpResponse('Login Success!')


def delete(req):
  print('Delete!')
  models.Users.objects.filter(username='432').delete()
  return HttpResponse('Delete Success!')


def update(req):
  print('Update!')
  models.Users.objects.filter(id='9').update(password='456')
  return HttpResponse('Update Success!')


def show(req):
  print('Show!')
  result = models.Users.objects.all()  # select * from table_name
  data = {
	  'userinfo': result[0].username,
  }
  return HttpResponse(json.dumps(data, ensure_ascii=False), 
								content_type="applicFation/json",
								charset='utf-8', status='200',
								reason='success')

# Create your views here.
