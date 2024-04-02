from django.urls import path
from . import views

urlpatterns = [
    path('phonex/', views.phonex, name='phonex'),
    path('About/', views.About, name='About'),
    path('contact/', views.contact, name='contact'),
    
    path('phones/', views.phones, name='phones'),
    path('login/', views.login, name='login'),
    path('register/', views.register, name='register'),
    path('home/', views.home, name='home'),
    path('sellphone/', views.sellphone, name='sellphone'),
    
    
    
   
]