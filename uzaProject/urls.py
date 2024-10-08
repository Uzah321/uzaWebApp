"""
URL configuration for uzaProject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from operator import index
from django.contrib import admin
from django.urls import path, include
from uzaApp import views
from django.conf.urls.static import static
from django.conf import settings
from user import views as user_view
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path('admin/', admin.site.urls),
    path('home/', views.index, name='dashboard-index'),
    path('staff/', views.staff, name='dashboard-staff'),
    path('staff/detail/<int:pk>/', views.staff_detail, name='dashboard-staff_detail'),
    path('product/', views.product, name='dashboard-product'),
    path('product/delete/<int:pk>/', views.product_delete, name='dashboard-product-delete'),
    path('product/update/<int:pk>/', views.product_update, name='dashboard-product-update'),
    path('order/', views.order, name='dashboard-order'),
    path('register/', user_view.register, name='register'),
    path('profile/', user_view.profile, name='user-profile'),
    path('user/profile/update/', user_view.profile_update, name='user-profile-update'),
    path('logout/', views.logout, name='user-logout'),
    path('', views.login_view, name='user-login'),
    #path('user/', include('user.urls')),
    #path('', include('uzaApp.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)    

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

  