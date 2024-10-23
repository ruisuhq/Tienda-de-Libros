from django import forms
from django.contrib.auth.forms import UserChangeForm
from .models import UserProfile

class EditProfileForm(UserChangeForm):
    class Meta:
        model = UserProfile
        fields = ['username', 'email', 'profile_image', 'description']
