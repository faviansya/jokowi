from django.shortcuts import render, redirect
from .models import Posting
# Create your views here.


def home(request):
    dbHome = Posting.objects.all()
    data = {
        'halamanhome': '/',
        'kontenhome': dbHome,
    }
    return render(request, 'home.html', data)

def lengkap(request, blog_id):
    dbHome = Posting.objects.get(pk=blog_id)
    data = {
        'halamanhome': '/',
        'kontenhome': dbHome,
    }
    return render(request, 'fullpage.html', data)


def beritalengkap(request):
    dbHome = Posting.objects.all()
    data = {
        'halamanhome': '/',
        'kontenberita': dbHome,
    }
    return render(request, 'beritalengkap.html', data)