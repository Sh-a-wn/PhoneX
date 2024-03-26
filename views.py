from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

def phonex(request):
    template = loader.get_template('homepage.html')
    return HttpResponse(template.render())

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')
    # Define more views as needed