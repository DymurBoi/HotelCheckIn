from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='sortingroom'

urlpatterns = [
    path('', views.room_category, name='room_category'),
    path('rooms/', views.room_category, name='room_category'),
    path('reserve_room/<int:roomId>/', views.reserve_room, name='reserve_room'),
    path('payment/<int:reservation_id>/<str:total_cost>/', views.payment_page, name='payment_page'),
    path('payment_confirmed/<int:payment_id>/', views.payment_confirmed, name='payment_confirmed'),
]