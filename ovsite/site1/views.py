from django.shortcuts import render
from .models import Task

def index(request):
    return render(request, 'index.html')

def add_item(request):
    if request.method == 'POST':
        task = Task()
        task.name = request.POST.get('name')
        task.text = request.POST.get('text')
        task.time = 121
        task.save()
        for i in Task.objects.all():
            i.info()

    return render(request, 'addItem.html')
