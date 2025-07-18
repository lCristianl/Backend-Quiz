from django.urls import path
from .views import QuizListAPIView, QuizDetailAPIView

urlpatterns = [
    path('quizzes/', QuizListAPIView.as_view(), name='quiz-list'),
    path('quizzes/<int:id>/', QuizDetailAPIView.as_view(), name='quiz-detail'),
]