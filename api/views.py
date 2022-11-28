import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from .serializer import NoteSerializer
from .models import Note

@api_view(['GET'])
def notes(request):
    query_set = Note.objects.all()
    serializer = NoteSerializer(query_set, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def get_note(request, pk):
    query_set = Note.objects.filter(pk=pk).get()
    serializer = NoteSerializer(query_set)
    return Response(serializer.data)
    