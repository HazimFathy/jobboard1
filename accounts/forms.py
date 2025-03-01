from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import get_user_model
from .models import Profile

# signup form
User = get_user_model()

class SignUpForm(UserCreationForm):
    email = forms.EmailField(max_length=254, help_text='Required. Enter a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2')
   
#user form
class UserForm(forms.ModelForm):
    class Meta:
        model= User
        fields=['first_name','last_name','email']
   
#profile form     
class profileform(forms.ModelForm):
    class Meta:
        model = Profile
        fields='__all__'
        exclude=('user', 'jobs',)


