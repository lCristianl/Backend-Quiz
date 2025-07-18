from django.shortcuts import render

# Create your views here.
from rest_framework import generics
from .models import Quiz
from .serializers import QuizSerializer, QuizDetailSerializer
from django.http import JsonResponse

class QuizListAPIView(generics.ListAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizSerializer

class QuizDetailAPIView(generics.RetrieveAPIView):
    queryset = Quiz.objects.all()
    serializer_class = QuizDetailSerializer
    lookup_field = 'id'

def home(request):
    return JsonResponse({
        'message': 'Django Quiz API is running successfully',
        'status': 'success',
        'endpoints': {
            'admin': '/admin/',
            'api': '/api/',
            'quizzes': '/api/quizzes/'
        }
    })