from django.shortcuts import render
from .models import Todolist

def index(request):
    todo_items = Todolist.objects.order_by('id')
    context = {'Todo_items' : todo_items}
    return  render(request,'todolist/index.html',context)
