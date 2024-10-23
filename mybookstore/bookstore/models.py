from django.contrib.auth.models import AbstractUser
from django.db import models

class UserProfile(AbstractUser):
    profile_image = models.ImageField(upload_to='profile_images/', null=True, blank=True)
    description = models.TextField(max_length=500, blank=True, null=True)

class CartItem(models.Model):
    user = models.ForeignKey(UserProfile, on_delete=models.CASCADE)
    book_id = models.CharField(max_length=100)
    quantity = models.IntegerField(default=1)
    
    def __str__(self):
        return f"{self.user.username} - {self.book_id}"