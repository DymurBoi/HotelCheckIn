from django.urls import path
from . import views

urlpatterns = [
    path('', views.room_list, name='room_list'),
    path('rooms/', views.room_list, name='room_list'), 
    path('reserve_room/<int:room_id>/', views.reserve_room, name='reserve_room'),
    path('payment/<int:reservation_id>/<str:total_cost>/', views.payment_page, name='payment_page'),
]