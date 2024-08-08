from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from .forms import CreateUserForm, LoginForm, UserUpdateForm, ProfileUpdateForm
# Create your views here.
def register(request):
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('user-login')
    else:
        form = CreateUserForm()            
    context = {
        'form': form
    }
    return render(request, 'user/register.html',context)  

def logout(request):
    auth.logout(request) 
    messages.success(request, 'You have been Logged out')
    return redirect('user-logout') 


def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                # Redirect to dashboard page after successful login
                return redirect('dashboard-index')  # Replace 'dashboard' with your dashboard URL name
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'user/login.html', {'form': form})
            
def profile(request):
    return render(request, 'user/profile.html')      

def profile_update(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(request.POST, instance=request.user)
        profile_form = ProfileUpdateForm( request.POST, request.FILES, instance=request.user.profile)
    else:
        user_form =  UserUpdateForm(instance=request.user)
        profile_form =  ProfileUpdateForm(instance=request.user.profile)  
    context = {
        'use_form':user_form,
        'profile_form':profile_form,
    }
    return render(request, 'user/profile_update.html', context)      