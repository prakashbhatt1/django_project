#this is view page 
from django.shortcuts import render
from .models import TodoItem
from django.http import HttpResponseRedirect
#we just creat an object to store all todo items

def todoView(request):
	all_todo_items = TodoItem.objects.all()
	return render(request,'todo.html',{'all_items': all_todo_items })

def addTodo(request):
	new_item=TodoItem(content = request.POST['content'])
	new_item.save()
	return HttpResponseRedirect('/Todo/')

def deleteTodo(request, todo_id):
	item_to_delete = TodoItem.objects.get(id=todo_id)
	item_to_delete.delete()
	return HttpResponseRedirect('/Todo/')
