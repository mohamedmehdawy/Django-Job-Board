from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import SignUpForm
from .models import Profile
from django.contrib.auth import authenticate, login

# Create your views here.

def SignUp(request):
    
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('jobs:job_list'))
    else:
        form = SignUpForm()
    context = {
        'form': form
    }
    return render(request, "registration/signup.html", context)


def profile(request):
    user_profile = Profile.objects.get(user=request.user)
    context = {
        "profile": user_profile
    }
    return render(request, "accounts/profile.html", context)


def profile_edit(request):
    pass