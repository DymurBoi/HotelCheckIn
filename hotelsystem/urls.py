"""
URL configuration for hotelsystem project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf.urls.static import static
from django.conf import settings 

urlpatterns = [
   path('admin/', admin.site.urls),  # Admin Dashboard
    path('account/', include('accounts.urls', namespace='account')),  # User Accounts (Signup, Login, etc.)
    path('dashboard/', include('dashboard.urls')),  # Admin Dashboard for managing the system
    path('rooms/<int:pk>', include('sortingroom.urls', namespace='sortingroom')),  # Room Management
    path('profile/', include('updateprofile.urls', namespace='profile')),  # User Profile Management
    path('', include('accounts.urls')),  # Default Home (from accounts)
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)