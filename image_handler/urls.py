from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='site-home'),
    path('upload/', views.upload_image,name='upload_image'),
    path('assign-label/<int:pk>/', views.assign_label,name='assign_label'),
    path('label-assigned/', views.label_assigned, name='label_assigned'),
    path('edit_label/<int:pk>/', views.edit_label, name='edit_label'),
    path('view-uploaded-images/', views.view_uploaded_images, name='view_uploaded_images'),
    path('signup/', views.SignUpView.as_view(), name='signup'),
    path('accounts/login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
