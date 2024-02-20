from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def upload(request):
    return render(request, 'upload.html')

def logo(request):
    return render(request, 'index.html')

def error(request):
    return render(request, 'index.html')

def complete(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'index.html')