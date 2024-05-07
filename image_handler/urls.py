from django.urls import path
from . import views

urlpatterns = [
    path('', views.home,name='site-home'),
    path('upload/', views.upload_image,name='upload_image'),
    path('assign-label/<int:pk>/', views.assign_label,name='assign_label'),
    path('label-assigned/', views.label_assigned, name='label_assigned'),
]

from django.conf import settings
from django.conf.urls.static import static

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
