from .models import UserStats
from django.contrib.auth.models import User
from django import forms

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    
    class Meta:
        model = User
        fields = ('username', 'email', 'password')
        
class UserStatsForm(forms.ModelForm):
    class Meta:
        model = UserStats
        fields = ('picture',)