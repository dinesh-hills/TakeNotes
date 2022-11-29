from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.notes),
    path('note/<int:pk>/', views.get_note),
    path('note/<int:pk>/update', views.get_note),
]
