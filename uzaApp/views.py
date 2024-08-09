from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.urls import reverse
from user.forms import LoginForm
from django.contrib.auth.decorators import login_required
from .models import Product
from .forms import ProductForm

@login_required(login_url='user-login')
def index(request):
    return render(request, 'dashboard/index.html')

@login_required(login_url='user-login')
def staff(request):
    return render(request, 'dashboard/staff.html')

@login_required(login_url='user-login')
def product(request):
    items = Product.objects.all()

    if request.method =='POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('dashboard-product')
    else:
        form = ProductForm()

    context = {
        'items': items,
        'form': form,
    }
    return render(request, 'dashboard/product.html', context)

@login_required(login_url='user-login')
def order(request):
    return render(request, 'dashboard/order.html')

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
                return redirect('dashboard-index')  # Replace 'dashboard-index' with your dashboard URL name
            else:
                form.add_error(None, 'Invalid username or password.')
    else:
        form = LoginForm()
    
    return render(request, 'user/login.html', {'form': form})

def logout_view(request):
    logout(request)
    return redirect(reverse('user-logout'))



#@login_required(login_url='user-login')
#@allowed_users(allowed_roles=['Admin'])
def product_delete(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
        return redirect('dashboard-product')
    context = {
        'item': item
    }
    return render(request, 'dashboard/product_delete.html', context)

#@login_required(login_url='user-login')
#@allowed_users(allowed_roles=['Admin'])
def product_update(request, pk):
    item = Product.objects.get(id=pk)
    if request.method == 'POST':
        form = ProductForm(request.POST, instance=item)
        if form.is_valid():
            form.save()
            return redirect('dashboard-products')
    else:
        form = ProductForm(instance=item)
    context = {
        'form': form,
    }
    return render(request, 'dashboard/product_update.html', context)