from django.urls import path
from . import views

urlpatterns = [
  path('login/', views.login),
  path('delete/', views.delete),
  path('update/', views.update),
  path('show/',views.show),
]