from django.urls import path
from . import views

urlpatterns = [
    # Event
    path('', views.event_list, name='event_list'),
    path('event/<int:pk>/', views.event_detail, name='event_detail'),
    path('event/add/', views.event_create, name='event_create'),
    path('event/<int:pk>/edit/', views.event_update, name='event_update'),
    path('event/<int:pk>/delete/', views.event_delete, name='event_delete'),

    # Participant
    path('participant/add/', views.participant_create, name='participant_create'),
    path('participant/<int:pk>/edit/', views.participant_update, name='participant_update'),
    path('participant/<int:pk>/delete/', views.participant_delete, name='participant_delete'),
    path('participant/', views.participant_list, name='participant_list'),
    # Category
    path('category/add/', views.category_create, name='category_create'),
    path('category/<int:pk>/edit/', views.category_update, name='category_update'),
    path('category/<int:pk>/delete/', views.category_delete, name='category_delete'),

    # Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),
]