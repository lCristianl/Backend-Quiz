from django.db import models

# Create your models here.
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()

    def __str__(self):
        return self.title

class Question(models.Model):
    QUESTION_TYPES = [
        ('text', 'Respuesta abierta'),
        ('multiple_choice', 'Opción múltiple'),
        ('true_false', 'Verdadero/Falso'),
    ]

    quiz = models.ForeignKey(Quiz, related_name='questions', on_delete=models.CASCADE)
    question_text = models.TextField()
    correct_answer = models.TextField()
    question_type = models.CharField(max_length=20, choices=QUESTION_TYPES, default='text')
    options = models.JSONField(blank=True, null=True)

    def __str__(self):
        return f"{self.quiz.title} - {self.question_text[:50]}"