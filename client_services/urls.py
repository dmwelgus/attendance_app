from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path(r'^clients/', views.clients, name='clients'),
    path(r'^clients/new_client/', views.new_clients.as_view(), name='new_client'),
    path(r'^programs/', views.program_list, name='programs'),
    path(r'^programs/new_program/', views.new_program.as_view(), name='new_program'),
    path(r'^sessions/', views.session_list, name='sessions'),
    path(r'^sessions/new_session/', views.new_session.as_view(), name='new_session'),
    path(r'^attendance/', views.take_attendance, name='attendance')
]
