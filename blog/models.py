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

class quis(models.Model):
  choice=[(0,'ya'),(1, 'tidak')]
  a1 = models.IntegerField(verbose_name = "Apakah kamu merasa malas (atau bahkan sangat malas) untuk mengerjakan tugas-tugas?",choices=choice,default= None)
  b1 = models.IntegerField(verbose_name = "Apakah kamu merasa takut untuk memulai tugas? ",choices=choice,default= None)
  c1 = models.IntegerField(verbose_name = "Apakah kamu sering merasa tidak mampu mengerjakan tugas?",choices=choice,default= None)
  d1 = models.IntegerField(verbose_name = "Apakah kamu sering menganggap remeh tugas?",choices=choice,default= None)
  e1 = models.IntegerField(verbose_name = "Apakah kamu kesulitan membagi waktu?",choices=choice,default= None)
  f1 = models.IntegerField(verbose_name = "Apakah kamu selalu menunggu menit terakhir pengumpulan tugas karena kamu merasa lebih baik jika bekerja dibawah tekanan?",choices=choice,default= None)
  g1 = models.IntegerField(verbose_name = "Apakah kamu merasa kesulitan untuk menentukan prioritas",choices=choice,default= None)
  h1 = models.IntegerField(verbose_name = "Apakah kamu kesulitan keluar dari zona nyaman?",choices=choice,default= None)
  i1 = models.IntegerField(verbose_name = "Kenapa kamu merasa takut untuk berinteraksi? Apakah karena merasa kurang pede?",choices=choice,default= None)
  j1 = models.IntegerField(verbose_name = "Apakah karena takut akan pandangan orang lain terhadap dirimu?",choices=choice,default= None)
  k1 = models.IntegerField(verbose_name = "Apakah merasa rendah diri  menjadi faktor anda untuk sulit berinteraksi?",choices=choice,default= None)
  l1 = models.IntegerField(verbose_name = "Apakah karena tidak ada orang yang sefrekuensi disekitarmu ?",choices=choice,default= None)
  m1 = models.IntegerField(verbose_name = "Apakah karena kejadian di masa lampau membuatmu sulit berinteraksi dengan lingkungan sekitarmu?",choices=choice,default= None)
  n1 = models.IntegerField(verbose_name = "Apakah anda masih merasa takut untuk memulai interaksi?",choices=choice,default= None)
  o1 = models.IntegerField(verbose_name = "Apakah kamu saat ini berada di lingkungan yang menurutmu baru?",choices=choice,default= None)
  p1 = models.IntegerField(verbose_name = "Apakah kamu merasa ada di lingkungan pertemanan yang buruk?",choices=choice,default= None)
  q1 = models.IntegerField(verbose_name = "Apakah kamu merasa ada teman yang mungkin bisa menjadi lebih dekat, tetapi kamu tidak yakin bagaimana mendekatinya?",choices=choice,default= None)
  r1 = models.IntegerField(verbose_name = "Apakah kamu merasa minder, rendah diri atau takut untuk memulai pertemanan?",choices=choice,default= None)
  s1 = models.IntegerField(verbose_name = "Apakah baru-baru ini kamu kehilangan seseorang/sesuatu yang menurutmu berharga? (Dan tidak memungkinkan untuk mengembalikannya)",choices=choice,default= None)
  def __str__(self):
    return self.k
  

  