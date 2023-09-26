from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

result = ['I','S','T','J']
quisans = ['a1', 'c1', 'g1']

def home(request):
  return render (request, 'blog/homepage.html' )

def about(request):
  return render (request, 'blog/about.html', {'title' : 'About'})

def rc(request):
  return render(request, 'blog/Room_chat.html', {'title' : 'RoomChat'})

def test(request):
  result.clear()
  if request.method == 'POST':
    form1 = ContactForm1(request.POST)
    form2 = ContactForm2(request.POST)
    form3 = ContactForm3(request.POST)
    form4 = ContactForm4(request.POST)
    if form1.is_valid() and form2.is_valid()and form3.is_valid() and form4.is_valid() :
      a = form1.cleaned_data
      def x1():
        x = a['a'] + a['b'] + a['c'] + a['d'] + a['e'] 
        if x > 2:
          result.append('I')
        else :
          result.append('E')
      f = form2.cleaned_data
      def x2():
        x = f['f'] + f['g'] + f['h'] + f['i'] + f['j'] 
        if x > 2:
          result.append('N')
        else :
          result.append('S')
      k = form3.cleaned_data
      def x4():
        x = p['p'] + p['q'] + p['r'] + p['s'] + p['t'] 
        if x > 2:
          result.append('F')
        else :
          result.append('T')
      def x3():
        x = k['k'] + k['l'] + k['m'] + k['n'] + k['o'] 
        if x > 2:
          result.append('P')
        else :
          result.append('J')
      p = form4.cleaned_data
      x1()
      x2()
      x4()
      x3()

      return render (request, 'blog/result.html', {'hasil' : ''.join(result)})
    #                    var aba = "{{aba}}";
    #                if(aba == 'none'){
     #                   document.getElementById("mountainb").style.display = "none";
      #              }

    
  else:
    form1 = ContactForm1()
    form2 = ContactForm2()
    form3 = ContactForm3()
    form4 = ContactForm4()
  return render(request, 'blog/mbti_test.html', {'form1' : form1,'form2' : form2,'form3' : form3,'form4' : form4, 'title' : 'MBTI test'})

def hasil(request):
  return render (request, 'blog/result.html', {'hasil' : ''.join(result),
                                               'aba' : 'none'})

def loli(request):
  return render (request, 'blog/loli.html')

def quisi(request):
  quisans.clear()
  if request.method == 'POST':
    form = Quis(request.POST)
    if form.is_valid():
      a = form.cleaned_data
      for i in a:
        if a[i] == 0:
          quisans.append(i)

      return render (request, 'blog/quires.html', {'quisans' : ','.join(quisans)})
     
  else:
    form = Quis()
  return render(request, 'blog/quis.html', {'form' : form})

def res(request):
  return render (request, 'blog/quires.html', {'quisans' : ','.join(quisans)})
