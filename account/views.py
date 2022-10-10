from django.shortcuts import render, redirect
from .forms import UserRegistrationForm, LoginForm
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def user_registration(request):
    form = UserRegistrationForm(request.POST or None)
    if form.is_valid():
        new_user = form.save(commit=False)
        new_user.set_password(form.cleaned_data['password'])
        new_user.save()
        return render(request, 'registration_done.html', context={'username': new_user.username})

    return render(request, 'registration.html', context={'form': form})


def user_login(request):
    form = LoginForm(request.POST or None)
      
    if form.is_valid():
        username, password = request.POST.get('username'), request.POST.get('password')
        user = authenticate(username=username, password=password)
        login(request, user)
        next_get = request.GET.get('next')
        next_post = request.POST.get('next')
        return redirect(next_post or next_get or '/')

    return render(request, 'login.html', context={'form': form})


def user_logout(request):
    logout(request)
    return redirect('/')


 