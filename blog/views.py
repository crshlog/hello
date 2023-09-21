from django.shortcuts import render
from django.http import HttpResponse
from .forms import *

result = []

def home(request):
  return render (request, 'blog/homepage.html',)

def about(request):
  return render (request, 'blog/about.html',)

def rc(request):
  return render(request, 'blog/Room_chat.html')

def test(request):
  
  if request.method == 'POST':
    form1 = ContactForm1(request.POST)
    form2 = ContactForm2(request.POST)
    form3 = ContactForm3(request.POST)
    form4 = ContactForm4(request.POST)
    if form2.is_valid():
      title = form2.cleaned_data
      result.append(title['a'])
      return render (request, 'blog/home.html', {'title' : result})
    
  else:
    form2 = ContactForm2()
  return render(request, 'blog/mbti_test.html', {'form2' : form2 })