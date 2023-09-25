from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from .choice import *

class tanya1(models.Model):
  def question(i):
    choice=[(0,question[i][0]),
      (1, question[i][1])]
    return choice
  a = models.IntegerField(verbose_name = "pertanyaan 1",choices=question(0),default= None)
  b = models.IntegerField(verbose_name = "pertanyaan 2",choices=question(1),default= None)
  c = models.IntegerField(verbose_name = "pertanyaan 3",choices=question(2),default= None)
  d = models.IntegerField(verbose_name = "pertanyaan 4",choices=question(3),default= None)
  e = models.IntegerField(verbose_name = "pertanyaan 5",choices=question(4),default= None)
  
  def __str__(self):
    return self.f

class tanya2(models.Model):
  def question(i):
    choice=[(0,question[i][0]),
      (1, question[i][1])]
    return choice
  f = models.IntegerField(verbose_name = "pertanyaan 6",choices=question(5),default= None)
  g = models.IntegerField(verbose_name = "pertanyaan 7",choices=question(6),default= None)
  h = models.IntegerField(verbose_name = "pertanyaan 8",choices=question(7),default= None)
  i = models.IntegerField(verbose_name = "pertanyaan 9",choices=question(8),default= None)
  j = models.IntegerField(verbose_name = "pertanyaan 10",choices=question(9),default= None)
  def __str__(self):
    return self.f

class tanya3(models.Model):
  def question(i):
    choice=[(0,question[i][0]),
      (1, question[i][1])]
    return choice
  k = models.IntegerField(verbose_name = "pertanyaan 11",choices=question(10),default= None)
  l = models.IntegerField(verbose_name = "pertanyaan 12",choices=question(11),default= None)
  m = models.IntegerField(verbose_name = "pertanyaan 13",choices=question(12),default= None)
  n = models.IntegerField(verbose_name = "pertanyaan 14",choices=question(13),default= None)
  o = models.IntegerField(verbose_name = "pertanyaan 15",choices=question(14),default= None)
  def __str__(self):
    return self.k
  
class tanya4(models.Model):
  def question(i):
    choice=[(0,question[i][0]),
      (1, question[i][1])]
    return choice
  p = models.IntegerField(verbose_name = "pertanyaan 16",choices=question(15),default= None)
  q = models.IntegerField(verbose_name = "pertanyaan 17",choices=question(16),default= None)
  r = models.IntegerField(verbose_name = "pertanyaan 18",choices=question(17),default= None)
  s = models.IntegerField(verbose_name = "pertanyaan 19",choices=question(18),default= None)
  t = models.IntegerField(verbose_name = "pertanyaan 20",choices=question(19),default= None)
  def __str__(self):
    return self.k


  

  