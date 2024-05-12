from django.shortcuts import redirect, render
from .forms import TodoForm

from .models import Todo

def todo_list(request):
    todos = Todo.objects.filter(completed=False)
    return render(request, 'todo/todo_list.html', {'todos': todos})

def todo_detail(request, pk):
    todo = Todo.objects.get(id=pk)
    return render(request, 'todo/todo_detail.html', {'todo': todo})

def todo_post(request):
    if request.method == "POST":
        form = TodoForm(request.POST)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm()
    return render(request, 'todo/todo_post.html', {'form': form})

def todo_edit(request, pk):
    todo = Todo.objects.get(id=pk)
    if request.method == "POST":
        form = TodoForm(request.POST, instance=todo)
        if form.is_valid():
            todo = form.save(commit=False)
            todo.save()
            return redirect('todo_list')
    else:
        form = TodoForm(instance=todo)
    return render(request, 'todo/todo_edit.html', {'form': form})

def todo_done(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = True
    todo.save()
    return redirect('todo_list')

def todo_done_list(request):
    dones = Todo.objects.filter(completed=True)
    return render(request, 'todo/todo_done_list.html', {'dones': dones})

def todo_delete(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.delete()
    return redirect('todo_done_list')

def todo_rollback(request, pk):
    todo = Todo.objects.get(id=pk)
    todo.completed = False
    todo.save()
    return redirect('todo_list')