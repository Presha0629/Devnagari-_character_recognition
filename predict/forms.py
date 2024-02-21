# forms.py
from django import forms
from django.forms import ModelForm
from .models import Character

class ImageUploadForm(forms.ModelForm):
    class Meta():
        model = Character
        fields = ["image","actual_character"]
