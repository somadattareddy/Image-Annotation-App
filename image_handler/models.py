from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class UploadedImage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    image = models.ImageField(upload_to='images/')
    label = models.CharField(max_length=100, blank=True)
