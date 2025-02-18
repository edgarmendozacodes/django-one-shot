from django.shortcuts import render
from todos.models   import TodoList
from todos.models   import TodoItem

# Create your views here.
def todo_list(request):
    todo_list = TodoList.objects.all()
    context = {
        "todo_list": todo_list,
    }
    return render(request, "todos/todos.html", context)

# def show_model_name(request):
#   model_list = ModelName.objects.all()
#   context = {
#     "model_list": model_list
#   }
#   return render(request, "model_names/list.html", context)
