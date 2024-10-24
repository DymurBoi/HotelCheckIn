from django.urls import path
from . import views

urlpatterns = [
    path('', views.HomePageView, name='homepage'),
    path('signup/', views.register, name='signup'), 
    path('login/',views.login_view, name='login'),
    path('success/', views.SuccessPageView, name='success'),
]
