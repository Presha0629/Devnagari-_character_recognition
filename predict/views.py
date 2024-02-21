from django.shortcuts import render, redirect
from .forms import ImageUploadForm
# Create your views here.
def upload(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():

            return redirect('success_page') 
    else:
        form = ImageUploadForm()

    return render(request, 'upload.html', {'form': form})

def prediction(request):
    print(request.POST)
    return render(request, "prediction.html")