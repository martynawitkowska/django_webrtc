from django.urls import path

from . import views

app_name = 'signal_server'

urlpatterns = [
    path('create_room/', views.CreateRoomView.as_view(), name='create_room'),
    path('join_room/<int:room_id>/', views.JoinRoomView.as_view(), name='join_room'),
]
