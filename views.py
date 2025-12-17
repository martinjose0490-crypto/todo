from django.shortcuts import render, redirect, get_object_or_404
from .models import TodoItem

# Module 1: List and Create
def index(request):
    todos = TodoItem.objects.all()
    if request.method == "POST":
        # Logic to "Add New To-Do"
        subject = request.POST.get('subject')
        notes = request.POST.get('notes')
        TodoItem.objects.create(subject=subject, notes=notes)
        return redirect('index')
    return render(request, 'todo/index.html', {'todos': todos})

# Module 2: Update, View, Delete
def edit_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    if request.method == "POST":
        todo.subject = request.POST.get('subject')
        todo.notes = request.POST.get('notes')
        todo.save()
        return redirect('index')
    return render(request, 'todo/edit.html', {'todo': todo})

def delete_todo(request, pk):
    todo = get_object_or_404(TodoItem, pk=pk)
    todo.delete()
    return redirect('index')
