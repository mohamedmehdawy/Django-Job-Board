from django.contrib.auth.models import User
from .models import Profile
from django.contrib.auth.forms import UserCreationForm
from django.forms import ModelForm


class SignUpForm(UserCreationForm):
    class Meta:
        model = User
        fields= ["username", "email", "password1", "password2"]

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ["username", "first_name", "last_name", "email"]
    

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ["phone_number", "city", "image"]