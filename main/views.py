from django.http import HttpResponseRedirect
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

def addtask(request):
    if request.method == 'POST':
        form = forms.CreateTask(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect('/')  # Redirect to a success page or another view
    else:
        form = forms.CreateTask()

    return render(request, 'main/addtask.html', {'form': form})