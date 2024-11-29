from django import forms
from .models import UserProfile
from accounts.models import CustomUser
class ProfilePicForm(forms.ModelForm):
    profile_pic=forms.ImageField(label="Profile Picture")
    
    class Meta:
        model=UserProfile
        fields = ['profile_pic']
        widgets = {
            'profile_pic': forms.ClearableFileInput(attrs={'style': 'display: none;'}),
        }
class UserForm(forms.ModelForm):
    class Meta:
        model = CustomUser
        fields = ['firstname','lastname', 'username','address','phone_number', 'profile_pic']
        labels={
            'firstname':'First Name',
            'lastname':'Last Name', 
            'username':'Email',
            'address':'Address',
            'phone_number':'Phone Number', 
            'profile_pic':'Profile Picture'
        }
        widgets = {
                'profile_pic': forms.ClearableFileInput(attrs={
                'initial_text': '',
                'input_text': '',
                'clear_checkbox_label': '',
            }),
        }