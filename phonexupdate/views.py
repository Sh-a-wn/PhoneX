from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.template import loader
from .forms import RegistrationForm, LoginForm

def phonex(request):
    return render(request, 'homepage.html')
def About(request):
    return render(request, 'about.html')
def phones(request):
    return render(request, 'phones.html')
def register(request):
    return render(request, 'register.html')
def login(request):
    return render(request, 'login.html')
def sellphone(request):
    return render(request, 'sellphone.html')
def contact(request):
    return render(request, 'contact.html')
def home(request):
    return render(request, 'home.html')





def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegistrationForm()
    return render(request, 'register.html', {'form': form})

def login(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = register.objects.filter(username=username, password=password).first()
            if register:
                # Logic for successful login
                return redirect('dashboard')
            else:
                # Logic for failed login
                return render(request, 'login.html', {'form': form, 'error': 'Invalid credentials'})
    else:
        form = LoginForm()
    return render(request, 'login.html', {'form': form})
