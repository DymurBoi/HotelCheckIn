from django.urls import path
from . import views

app_name='profile'

urlpatterns = [
    path('', views.sample_home, name='home'),  
    path('user/<int:pk>/', views.user_list, name='user_profile'),  
    path('update/<int:pk>/', views.update_user, name='update_profile'), 
    path('sample/', views.sample,name='sample'),
]
