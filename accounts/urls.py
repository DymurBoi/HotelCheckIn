from django.urls import path
from . import views

app_name='account'

urlpatterns = [
    path('', views.HomePageView, name='homepage'),  # Default Homepage
    path('signup/', views.register, name='signup'),  # User Registration
    path('login/', views.login_view, name='login'),  # User Login
    path('success/', views.SuccessPageView, name='success'),  # Post-Action Success Page
]
