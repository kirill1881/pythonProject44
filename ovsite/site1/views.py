from django.shortcuts import render, redirect
from .models import Task
import time

def index(request):
    tasks = Task.objects.filter(flag=True)
    return render(request, 'index.html', {'tasks':tasks, 'arch':'Архив задач',
                                          'addto':'Добавить в архив',
                                          'link':'/archive'})

def archive(request):
    tasks = Task.objects.filter(flag=False)
    return render(request, 'index.html', {'tasks': tasks, 'arch': 'Текущие задачи',
                                          'addto': 'Востановить из архива',
                                          'link':'/'})

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

def acrh(request, id):
    task = Task.objects.filter(id=id)[0]
    if task.flag == True:
        task.flag = False
        Task.save(task)
        return redirect('/')
    else:
        task.flag = True
        Task.save(task)
        return redirect('/archive')



def add_item(request):
    if request.method == 'POST':
        task = Task()
        task.name = request.POST.get('name')
        task.text = request.POST.get('text')
        task.time = f'{time.gmtime().tm_mday}.{time.gmtime().tm_mon}'
        task.flag = True
        task.save()
        return redirect('/')

    return render(request, 'addItem.html')
