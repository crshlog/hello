from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django import forms
from .choice import *

class tanya1(models.Model):
  def question(i):
    choice=[('select1',question[i][0]),
      ('select2', question[i][1])]
    return choice
  a = models.CharField(verbose_name = "pertanyaan 1",choices=question(0), max_length=128, default=1)
  b = models.CharField(verbose_name = "pertanyaan 2",choices=question(1), max_length=128, default=1)
  c = models.CharField(verbose_name = "pertanyaan 3",choices=question(2), max_length=128, default=1)
  d = models.CharField(verbose_name = "pertanyaan 4",choices=question(3), max_length=128, default=1)
  e = models.CharField(verbose_name = "pertanyaan 5",choices=question(4), max_length=128, default=1)
  def __str__(self):
    return self.a

class tanya2(models.Model):
  def question(i):
    choice=[('select1',question[i][0]),
      ('select2', question[i][1])]
    return choice
  f = models.CharField(verbose_name = "pertanyaan 6",choices=question(5), max_length=128, default=1)
  g = models.CharField(verbose_name = "pertanyaan 7",choices=question(6), max_length=128, default=1)
  h = models.CharField(verbose_name = "pertanyaan 8",choices=question(7), max_length=128, default=1)
  i = models.CharField(verbose_name = "pertanyaan 9",choices=question(8), max_length=128, default=1)
  j = models.CharField(verbose_name = "pertanyaan 10",choices=question(9), max_length=128, default=1)
  def __str__(self):
    return self.a

class tanya3(models.Model):
  def question(i):
    choice=[('select1',question[i][0]),
      ('select2', question[i][1])]
    return choice
  k = models.CharField(verbose_name = "pertanyaan 11",choices=question(10), max_length=128, default=1)
  l = models.CharField(verbose_name = "pertanyaan 12",choices=question(11), max_length=128, default=1)
  m = models.CharField(verbose_name = "pertanyaan 13",choices=question(12), max_length=128, default=1)
  n = models.CharField(verbose_name = "pertanyaan 14",choices=question(13), max_length=128, default=1)
  o = models.CharField(verbose_name = "pertanyaan 15",choices=question(14), max_length=128, default=1)
  def __str__(self):
    return self.a
  
class tanya4(models.Model):
  def question(i):
    choice=[('select1',question[i][0]),
      ('select2', question[i][1])]
    return choice
  p = models.CharField(verbose_name = "pertanyaan 16",choices=question(15), max_length=128, default=1)
  q = models.CharField(verbose_name = "pertanyaan 17",choices=question(16), max_length=128, default=1)
  r = models.CharField(verbose_name = "pertanyaan 18",choices=question(17), max_length=128, default=1)
  s = models.CharField(verbose_name = "pertanyaan 19",choices=question(18), max_length=128, default=1)
  t = models.CharField(verbose_name = "pertanyaan 20",choices=question(19), max_length=128, default=1)
  def __str__(self):
    return self.a  


  

  