from django.urls import path
from . import views
from django.contrib.auth import views as auth_views

app_name='dashboard'

urlpatterns = [
    path('', views.welcome, name = 'welcome'),
    path('login/', views.admin_login, name='login'),
    path('admin_landing/', views.admin_landing, name='admin_landing'),
    path('logout/', views.admin_logout, name='admin_logout'),

    path('room/', views.add_or_modify_room, name='add_or_modify_room'),
    path('room/add/',views.add_room,name='add_room'),
    path('room/modify/', views.modify_room_landing, name='modify_room_landing'),
    path('room/modify/<int:room_id>/', views.room_detail, name='room_detail'),
    path('room/checkout/<int:room_id>/', views.check_out, name='check_out'),
    #path('modify_room/<int:room_id>/', views.modify_room, name='modify_room'),
    
    path('category/', views.add_or_modify_category, name='add_or_modify_category'),
    path('category/add/', views.add_category, name='add_category'),
    path('category/modify/', views.modify_category_landing, name='modify_category_landing'),
    path('category/modify/<int:id>/', views.modify_category, name='modify_category'),
]
