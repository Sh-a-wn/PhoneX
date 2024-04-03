from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brands, Make
from .forms import BrandsForm, RegistrationForm

# Create your views here.
def homepage(request):
    return render(request, 'homepage.html')

def brands(request):
    collected_data = Brands.objects.all()
    context = {'brands':collected_data}
    return render(request, 'brands.html')

def phone_details(request):
    return render(request, 'phone_details.html')

def dealer_login(request):
    # redirect('add_Brand.html')
    return render(request, 'dealer_login.html')

def user_login(request):
    return render(request, 'user_login.html')

def addBrand(request):
    form = BrandsForm

    if request.method == 'POST':
        form = BrandsForm(request.POST)
        if form.is_valid():
            form.save()
            redirect('brands')
    context = {'form': form}
    return render(request, 'add_Brand.html', context)

def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})


def sell_phone(request):
    form = BrandsForm

    if request.method == "POST":
        form = BrandsForm(request.POST)
        if form.is_valid():
            form.save()
    
    context = {'form': form}
    return render(request, 'sell_phone.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

def login(request):
    return render(request, 'login.html')

def forgot_password(request):
    return render(request, 'forgot_password.html')

def phones(request):
    return render(request, 'phones.html')