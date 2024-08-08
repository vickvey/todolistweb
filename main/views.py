from django.http import HttpResponseRedirect, HttpResponse
from django.shortcuts import render
from main import (
    models,
    forms
)

# Create your views here.
def index(request):
    if request.method == 'POST':
        # Get the list of checked task IDs from the POST request
        checked_task_ids = request.POST.getlist('tasks')
        
        # Update tasks based on IDs
        models.Task.objects.filter(id__in=checked_task_ids).update(done=True)
        
        return HttpResponseRedirect('/')  # Redirect to avoid resubmission issues

    tasks = models.Task.objects.filter(done=False)
    context = {
        'tasks': tasks,
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