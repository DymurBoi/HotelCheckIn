from django import forms
from .models import UserProfile

class ProfilePicForm(forms.ModelForm):
    profile_pic=forms.ImageField(label="Profile Picture")
    
    class Meta:
        model=UserProfile
        fields=['profile_pic',  ]

class UserForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['name', 'address','email','phone_num','password', 'profile_pic']