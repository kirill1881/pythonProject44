from django.shortcuts import render, redirect
from .models import Task
import time

def index(request):
    tasks = Task.objects.all()
    return render(request, 'index.html', {'tasks':tasks})

def edit_item(request, id):
    if request.method == 'GET':
        tasks = Task.objects.filter(id=id)[0]
        return render(request, 'EditItem.html', {'tasks':tasks})
    elif request.method == 'POST':
        task = Task.objects.filter(id=id)[0]
        task.name = request.POST.get('name')
        task.text = request.POST.get('text')
        Task.save(task)
        return redirect('/')

def delete_item(request, id):
    Task.objects.filter(id=id).delete()
    return redirect('/')

def add_item(request):
    if request.method == 'POST':
        task = Task()
        task.name = request.POST.get('name')
        task.text = request.POST.get('text')
        task.time = f'{time.gmtime().tm_mday}.{time.gmtime().tm_mon}'
        task.save()
        return redirect('/')

    return render(request, 'addItem.html')
