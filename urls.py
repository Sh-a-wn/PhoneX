from django.urls import path
from . import views

urlpatterns = [
    path('phonex/', views.phonex, name='phonex'),
    path('home/', views.home, name='home'),
    path('about/', views.about, name='about'),
   
]