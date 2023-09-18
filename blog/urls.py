from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='blog-home'),
    path('about/', views.about, name='blog-about'),
    path('web/', views.web, name='web'),
    path('room_chat/', views.rc, name='rc')
]