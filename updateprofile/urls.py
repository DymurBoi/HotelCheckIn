from django.urls import path
from . import views

app_name='profile'

urlpatterns = [
    path('<int:pk>/', views.sample_home, name='home'),  
    path('user/', views.user_profile, name='user_profile'),  
    path('update/', views.update_user, name='update_profile'),
    path('reservation_list/<int:pk>/', views.reservation_list, name='reservations'),  
    path('room/<int:pk>/', views.room_view, name='room_view'),  
    path('sample/', views.sample,name='sample'),
]
