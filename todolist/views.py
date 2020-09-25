from django.shortcuts import redirect, render
from .models import Todolist
from .forms import TodoListForm
from django.views.decorators.http import require_POST

def index(request):       # Rendering for the index page
    todo_items = Todolist.objects.order_by('id')
    form = TodoListForm()
    context = {'Todo_items' : todo_items, 'form' : form}
    return  render(request,'todolist/index.html',context)

@require_POST
def addTodoItem(request):              # Fetching todo item and adding it to database
    form = TodoListForm(request.POST)
    if form.is_valid():
        new_todo = Todolist(text=request.POST['text'])
        new_todo.save()
    return redirect('index')