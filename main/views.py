from django.shortcuts import render
from main import models

# Create your views here.
def index(request):
    tasks=models.Task.objects.all()
    context={
        'tasks': tasks
    }

    return render(request, 'main/index.html', context)