from django.urls import path
from . import views

app_name='profile'

urlpatterns = [
    path('user/', views.user_profile, name='user_profile'),  
    path('update/', views.update_user, name='update_profile'),
    path('reservation_list/', views.reservation_list, name='reservations'),
    path('logout/', views.logout_view, name='logout'),   
    path('cancel_reservation/<int:id>/', views.cancel_reservation, name='cancel_reservation'),
] 

