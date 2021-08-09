from django.shortcuts import render
from .models import Article

# Create your views here.
def home(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'index.html',{'article':article})

def homepage(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'index.html',{'article':article})

def technology(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'pages/technology.html',{'article':article})

def economy(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'pages/economy.html',{'article':article})

def sports(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'pages/sports.html',{'article':article})

def international(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'pages/international.html',{'article':article})


def news(request):
    article = Article.objects.all().order_by('-id')
    return render(request, 'pages/news.html',{'article':article})