from django.db import models
from django.conf import settings

# Create your models here.

class TodoList(models.Model):
    # This defines the fields of your model # 
    name = models.CharField(max_length = 100) # max length 100 characters
    created_on = models.DateTimeField(auto_now_add=True) # should be automatically set to the time the todolist was created
    # This tells Django how to convert model into a string 
    def __str__(self):
        return self.name  

class TodoItem(models.Model):
    task = models.CharField(max_length=100) 
    due_date = models.DateTimeField(
        null = True,
        blank = True,
    )
    is_completed = models.BooleanField(default=False)
    
    list = models.ForeignKey(
        TodoList,
        related_name = "items", 
        on_delete = models.CASCADE
    ) 
