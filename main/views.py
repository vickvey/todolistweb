from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from main import (
    models,
    forms
)

# Create your views here.
def index(request):
    tasks=models.Task.objects.all()
    context={
        'tasks': tasks
    }
    return render(request, 'main/index.html', context)

def add_task(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')
    else:
        form = forms.CreateTask()
    return render(request, 'main/add_task.html', {'form': form})

def completed_tasks(request):
    # Filter tasks where 'done' is True
    completed_tasks = models.Task.objects.filter(done=True)
    
    context = {
        'completed_tasks': completed_tasks
    }
    
    return render(request, 'main/completed_tasks.html', context)