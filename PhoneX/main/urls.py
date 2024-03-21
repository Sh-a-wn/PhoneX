from django.urls import path
from . import views

urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('home/', views.homepage, name='homepage'),
    path("brands/", views.brands, name="brands"),
    path('dealer_login/', views.dealer_login, name='dealer_login'),
    path('user_login/', views.user_login, name="user_login"),
    path('add-Brand/', views.addBrand, name='addBrand'),
    path('register/', views.register, name='register'),
    path('sell_phone/', views.sell_phone, name="sell_phone"),
    path('phone_details', views.phone_details, name="phone_details"),
]