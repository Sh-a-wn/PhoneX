from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Brands, Make
from .forms import BrandsForm

# Create your views here.
def home(request):
    return render(request, 'homepage.html')

def brands(request):
    collected_data = Brands.objects.all()
    context = {'brands':collected_data}
    return render(request, 'brands.html', context)

def dealer_login(request):
    redirect('add_Brand.html')
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