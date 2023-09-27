from django.urls import path

from . import views

app_name = 'signal_server'

urlpatterns = [
    path('create_room/', views.CreateRoomView.as_view(), name='create_room'),
    path('join_room/<int:room_id>/', views.JoinRoomView.as_view(), name='join_room'),
    path('create-offer/', views.CreateOfferView.as_view(), name='create_offer'),
    path('create-answer/', views.CreateAnswerView.as_view(), name='create_answer'),
    path('create-ice-candidate/', views.CreateIceCandidateView.as_view(), name='create_ice_candidate'),
]
