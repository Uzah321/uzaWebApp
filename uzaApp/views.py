from multiprocessing import AuthenticationError
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.urls import reverse
from user.forms import LoginForm


def index(request):
    return render(request, 'dashboard/index.html')

def staff(request):
    return render(request, 'dashboard/staff.html')

def product(request):
    return render(request, 'dashboard/product.html')

def order(request):
    return render(request, 'dashboard/order.html')

def register(request):
    return render(request, 'user/register.html')

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
                return redirect('home')  # Replace 'dashboard' with your dashboard URL name
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'user/login.html', {'form': form})
            
def Logout_view(request):
    logout(request)
    return redirect(reverse('login'))
