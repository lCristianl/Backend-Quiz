from django.http import JsonResponse

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