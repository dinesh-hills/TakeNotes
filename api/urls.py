from django.urls import path
from . import views

urlpatterns = [
    path('notes/', views.NotesList.as_view()),
    path('notes/<int:pk>/', views.NotesDetail.as_view()),
]
