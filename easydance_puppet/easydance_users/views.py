# 用户操作相关接口

import json
from django.http import HttpResponse
from . import models

def login(req):
    try:
        openid = req.GET.get('openid')
        result = models.Users.objects.get(openid=openid)
        check_result = {
            'nickName': result.nickName,
            'avatarUrl': result.avatarUrl,
            'country': result.country,
            'province': result.province,
            'gender': result.gender,
            'lanuage': result.lanuage,
            'city': result.city,
            'openid': result.openid,
        }
    except Exception:
        dic = {
            'nickName': req.GET.get('nickName'),
            'avatarUrl': req.GET.get('avatarUrl'),
            'country': req.GET.get('country'),
            'province': req.GET.get('province'),
            'gender': req.GET.get('gender'),
            'lanuage': req.GET.get('lanuage'),
            'city': req.GET.get('city'),
            'openid': req.GET.get('openid'),
        }
        users = models.Users(**dic)
        users.save()
        check_result = dic
    return HttpResponse(json.dumps(check_result, ensure_ascii=False),
                        content_type="application/json",
                        charset='utf-8',
                        status='200',
                        reason='success')

# Create your views here.
