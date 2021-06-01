from django import forms
from .models import Brands

class BrandCreateForm(forms.Form):
    brand_name=forms.CharField()


