from django.shortcuts import render, redirect
from .models import Task

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})

def delete_item(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')

def add_item(request):
    if request.method == 'POST':
        task = Task()
        task.name = request.POST.get('name')
        task.text = request.POST.get('text')
        task.time = 121
        task.save()
        return redirect('/')

    return render(request, 'addItem.html')
