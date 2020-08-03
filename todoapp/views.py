from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import ToDoForm
from .models import ToDo

def index_view(request):
    todos = ToDo.objects.all() # todo's
    return render(request, 'todoapp/index.html', {'todo_items' : todos})

def add_todo_view(request):
    if request.method == "POST":
        todo_form = ToDoForm(request.POST)
        if todo_form.is_valid():
            todo_form.save()
            return HttpResponseRedirect('/')
        else: return HttpResponse("<h1>Invalid Data</h1>")      
    return render(request, 'todoapp/add_todo.html', {'todo_form' : ToDoForm()})

def about_todo_view(request):
    return render(request, 'todoapp/about_todo.html', {})

def remove_todo_view(request):
    return render(request, 'todoapp/remove_todo.html', {})

# Create your views here.
