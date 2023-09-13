from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

post = [
    {'title' : 'post1',
     'when'  :'12 august',
     'where' :'my house'},
    {'title' : 'post2',
     'when'  :'14 august',
     'where' :'my mother\'s house'},
] 

# Create your views here.
def home(request):
  content = {'posts' : Post.objects.all(),
             'title' : 'homepage'}
  return render (request, 'blog/home.html', content, )

def about(request):
  return render (request, 'blog/about.html',  {'title': 'About'})

def web(request):
  return render(request, 'blog/web.html')