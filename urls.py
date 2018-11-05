#import your views first and set url path

from django.contrib import admin
from django.urls import path
from todo.views import todoView,addTodo,deleteTodo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('Todo/',todoView),
    path('deleteTodo/<int:todo_id>/',deleteTodo),
    path('addTodo/',addTodo),

]
