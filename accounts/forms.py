from django import forms
from .models import CustomUser

class CustomUserCreationForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput, label='Password')
    
    class Meta:
        model = CustomUser
        fields = ['username', 'firstname', 'lastname', 'phone_number', 'password']  # Include the necessary fields

    def save(self, commit=True):
        # Get the user object without saving to the database yet
        user = super(CustomUserCreationForm, self).save(commit=False)
        
        # Set the hashed password using set_password
        user.set_password(self.cleaned_data['password'])
        
        # Save the user object if commit is True
        if commit:
            user.save()
        
        return user
    
class CustomUserLoginForm(forms.Form):
    username = forms.EmailField(max_length=150)
    password = forms.CharField(widget=forms.PasswordInput,max_length=150)
