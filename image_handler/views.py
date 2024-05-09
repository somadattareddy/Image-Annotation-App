from django.shortcuts import render, redirect, get_object_or_404
from .forms import UploadImageForm
from .models import UploadedImage
from django.contrib.auth.decorators import login_required
from PIL import Image

def home(request):
    return render(request,'image_handler/home.html')

@login_required
def upload_image(request):
    if request.method == 'POST':
        form = UploadImageForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded_image = form.save(commit=False)
            uploaded_image.user = request.user
            uploaded_image.save()
            image_path = uploaded_image.image.path
            img = Image.open(image_path)
            resized_img = img.resize((600, 400)) 
            resized_img.save(image_path)
            return redirect('assign_label', pk=uploaded_image.pk)
    else:
        form = UploadImageForm()
    return render(request, 'image_handler/upload_image.html', {'form': form})

@login_required
def assign_label(request, pk):
    uploaded_image = get_object_or_404(UploadedImage, pk=pk, user=request.user)

    # Defining predefined label options
    label_options = ['Class 1', 'Class 2', 'Class 3']
    
    if request.method == 'POST':
        label = request.POST.get('label')
        uploaded_image.label = label
        uploaded_image.save()
        return redirect('label_assigned')
    
    return render(request, 'image_handler/assign_label.html', {'image': uploaded_image, 'label_options': label_options})

def label_assigned(request):
    return render(request, 'image_handler/label_assigned.html')

from django.http import JsonResponse

@login_required
def edit_label(request, pk):
    if request.method == 'POST':
        uploaded_image = get_object_or_404(UploadedImage, pk=pk, user=request.user)
        new_label = request.POST.get('new_label')
        uploaded_image.label = new_label
        uploaded_image.save()
        return redirect('view_uploaded_images')
    else:
        return JsonResponse({'success': False, 'error': 'Invalid request method'})

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic.edit import CreateView

class SignUpView(CreateView):
    form_class = UserCreationForm
    success_url = reverse_lazy('login')
    template_name = 'image_handler/signup.html'

login_view = LoginView.as_view(template_name='image_handler/login.html')
logout_view = LogoutView.as_view(next_page='/')

@login_required
def view_uploaded_images(request):
    images = UploadedImage.objects.filter(user=request.user)
    label_options = ['Class 1', 'Class 2', 'Class 3']
    return render(request, 'image_handler/view_uploaded_images.html', {'images': images, 'label_options': label_options})