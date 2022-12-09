from rest_framework import status
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializer import NoteSerializer
from .models import Note

class NotesList(APIView):
    
    def get(self, request):
        queryset = Note.objects.all()
        serializer = NoteSerializer(queryset, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        note = Note.objects.create(body=request.data['body'])
        serializer = NoteSerializer(note)
        return Response(serializer.data)
    
    
class NotesDetail(APIView):
    
    def get(self, request, pk):
        query_set = Note.objects.filter(pk=pk).get()
        serializer = NoteSerializer(query_set)
        return Response(serializer.data)
        
    def put(self, request, pk):
        note = Note.objects.get(pk=pk)
        serializer = NoteSerializer(note, data=request.data)
        serializer.is_valid()
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, pk):
        note = Note.objects.get(pk=pk)
        note.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)