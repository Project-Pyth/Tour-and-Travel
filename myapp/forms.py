from django import forms
from django.contrib.auth.forms import User
from myapp.models import PersonalProfile
from .models import UProfile

class UserUpdate(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email']

class ProfileUpdate(forms.ModelForm):
    class Meta:
        model = UProfile
        fields = ['dob', 'bio','city','image']



