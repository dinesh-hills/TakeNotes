from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.notes),
    path('notes/<int:pk>/', views.get_note),
]
