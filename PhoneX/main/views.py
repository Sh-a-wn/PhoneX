from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brands, Make
from .forms import BrandsForm, CreateNewUser
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages

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
    form = CreateNewUser()

    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/homepage')


    context = {'form' : form}
    return render(request, 'registerpage.html', context)

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
    form = CreateNewUser()

    if request.method == 'POST':
        form = CreateNewUser(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Account was created successfully')

            return redirect('login')

    context = {'form' : form}
    return render(request, 'register.html', context)


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

def loginPage(request):

    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user != None:
            login(request, user)
            return redirect('homepage')
        else:
            messages.info(request, 'Invalid username or password')

    context = {}
    return render(request, 'login.html', context)

def forgot_password(request):
    return render(request, 'forgot_password.html')

def phones(request):
    return render(request, 'phones.html')