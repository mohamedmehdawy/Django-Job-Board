from django.shortcuts import redirect, render
from django.urls import reverse

from .forms import SignUpForm, UserForm, ProfileForm
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
    user_profile = Profile.objects.get(user=request.user)
    if request.method == "POST":
        user_form = UserForm(request.POST, instance=request.user)
        profile_form = ProfileForm(request.POST, request.FILES, instance=user_profile)

        if user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse("accounts:profile"))
    else:
        user_form = UserForm(instance=request.user)
        profile_form = ProfileForm(instance=user_profile)
    context = {
        "user_form": user_form,
        "profile_form": profile_form
    }
    return render(request, "accounts/profile_edit.html", context)