#this is models where we just create a one attribute called content 
from django.db import models

class TodoItem(models.Model):
	content = models.TextField() 
