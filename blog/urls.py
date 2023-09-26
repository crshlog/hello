from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('home/', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('room_chat/', views.rc, name='rc'),
    path('test/', views.test, name='test'),
    path('result/', views.hasil, name='result'),
    path('no/no/no/no/no/loli/', views.loli, name='result'),
    path('quis/', views.quisi, name='result'),
    path('res/', views.res, name='result'),
]