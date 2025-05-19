from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login , get_user_model
from django.urls import reverse
from .forms import SignUpForm, profileform, UserForm
from .models import Profile
from django.http import HttpResponseForbidden



User = get_user_model()

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect(reverse('jobs:job_list'))
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


def profile_view(request):
    profile = get_object_or_404(Profile, user=request.user) 
    jobs = profile.jobs.all()
    return render(request, 'accounts/profile.html', {'profile': profile, 'jobs': jobs})


def profile_edit(request):
    profile = get_object_or_404(Profile, user=request.user)
    if request.method == 'POST':
        profile_form = profileform(request.POST, request.FILES, instance=profile)
        user_form = UserForm(request.POST, instance=request.user)
        if profile_form.is_valid() and user_form.is_valid():
            user_form.save()
            profile_form.save()
            return redirect(reverse('accounts:profile'))
    else:
        profile_form = profileform(instance=profile)
        user_form = UserForm(instance=request.user)
    
    return render(request, 'accounts/profile_edit.html', {
        'profileform1': profile_form,
        'userform1': user_form
    })



def custom_404(request, exception):
    return render(request, 'errors/404.html', status=404)
def custom_500(request):
    return render(request, "500.html", status=500)
