from django.forms import ModelForm
from .models import Brands

class BrandsForm(ModelForm):
    class Meta:
        model = Brands
        fields = ['name']