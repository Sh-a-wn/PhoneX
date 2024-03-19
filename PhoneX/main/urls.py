from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name= "home"),
    path('home/', views.home, name= 'home'),
    path("brands/", views.brands, name="brands"),
    path('dealer_login/', views.dealer_login, name='dealer_login'),
    path('user_login/', views.user_login, name="user_login"),
    path('add-Brand/', views.addBrand, name='addBrand'),
]