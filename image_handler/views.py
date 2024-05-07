# from django.shortcuts import render

# def home(request):
#     return render(request,'image_handler/home.html')

# def upload_image(request):
#     return render(request,'image_handler/upload.html')

# def annotate_image(request):
#     return render(request,'image_handler/annotate.html')

from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadImageForm
from .models import UploadedImage

def home(request):
    return render(request,'image_handler/home.html')

def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save()
            # Redirect to the label assignment page
            return redirect('assign_label', pk=uploaded_image.pk)
    else:
        form = UploadImageForm()
    return render(request, 'image_handler/upload_image.html', {'form': form})

def annotate_image(request):
    return render(request,'image_handler/annotate.html')

def assign_label(request, pk):
    uploaded_image = get_object_or_404(UploadedImage, pk=pk)

    # Define predefined label options
    label_options = ['Label 1', 'Label 2', 'Label 3']
    
    if request.method == 'POST':
        label = request.POST.get('label')
        uploaded_image.label = label
        uploaded_image.save()
        # Redirect to another page after assigning the label
        return redirect('label_assigned')
    
    return render(request, 'image_handler/assign_label.html', {'image': uploaded_image, 'label_options': label_options})

def label_assigned(request):
    return render(request, 'image_handler/label_assigned.html')
