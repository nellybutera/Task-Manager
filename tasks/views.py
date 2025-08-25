# tasks/views.py

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.contrib import messages

from .models import Task
from .forms import TaskForm, SignUpForm

@login_required
def task_list(request):
    # list the logged-in user's tasks
    tasks = Task.objects.filter(user=request.user).order_by('-created_at')
    return render(request, 'tasks/task_list.html', {'tasks': tasks})

@login_required
def task_create(request):
    if request.method == 'POST':
        form = TaskForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.user = request.user # ensure ownership
            task.save()
            messages.success(request, 'Task created.')
            return redirect('task_list')
    else:
        form = TaskForm()
        
    return render(request, 'tasks/task_form.html', {'form':form, 'title': 'New Task'})

@login_required
def task_update(request, pk):
    # edit an existing task (only if you own it).
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        form = TaskForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            messages.success(request, 'Task updated.')
            return redirect('task_list')
    else:
        form = TaskForm(instance=task)
        
    return render(request, 'tasks/task_form.html', {'form':form, 'title': 'Edit Task'})

@login_required
def task_delete(request, pk):
    #delete a task you own, with confirmation.
    task = get_object_or_404(Task, pk=pk, user=request.user)
    if request.method == 'POST':
        task.delete()
        messages.success(request, 'Task deleted.')
        return redirect('task_list')
    return render(request, 'tasks/task_confirm_delete.html', {'task':task})

@login_required
def task_toggle_complete(request, pk):
    # quickly toggle completed True/False
    task = get_object_or_404(Task, pk=pk, user=request.user)
    task.completed = not task.completed
    task.save()
    return redirect('task_list')

def signup(request):
    # register a new user and log them in
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, 'Welcome! Account created.')
            return redirect('task_list')
    else:
        form = SignUpForm()
        
    return render(request, 'registration/signup.html', {'form': form})