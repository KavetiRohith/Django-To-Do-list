from django.shortcuts import render,redirect
from django.http import HttpResponse

from .models import *
from .forms import *
# Create your views here.

def homepage(request):
    tasks = task.objects.all()
    
    form = taskForm()

    if request.method =='POST':
        form = taskForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('/')

    context = {'tasks':tasks, 'form':form}
    return render(request, 'tasks/index.html' ,context)


def updateTask(request, pk):
    temp = task.objects.get(id=pk)

    form =taskForm(instance = temp)

    if request.method =="POST":
        form =taskForm(request.POST,instance = temp)
        if form.is_valid:
            form.save()
            return redirect('/')

    context = {'form':form}

    return render(request, 'tasks/update_task.html', context)


def deleteTask(request, pk):
    item = task.objects.get(id=pk)

    if request.method =="POST":
        item.delete()
        return redirect('/')

    context = { 'item':item }

    return render(request, 'tasks/delete.html',context)