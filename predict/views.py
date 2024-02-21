from django.shortcuts import render, redirect
from .forms import ImageUploadForm
from django.urls import reverse
# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            posted = form.save(commit=False)
            posted.save()
            return redirect(reverse('predict:prediction')) 
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

def prediction(request):
    print(request.POST)
    return render(request, "prediction.html")