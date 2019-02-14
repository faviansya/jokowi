from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('beritalengkap', views.beritalengkap, name='beritalengkap'),
    path('<int:blog_id>', views.lengkap, name='fullpage'),
]
