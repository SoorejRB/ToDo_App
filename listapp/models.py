
from django.db import models
from django.contrib.auth.models import User
import datetime

class BaseDateTime(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class TaskType(BaseDateTime):
    name = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.name

class Task(BaseDateTime):
    title = models.CharField(max_length=100)
    description = models.TextField(null=True, blank=True)
    priority = models.PositiveIntegerField(null=True, blank=True)
    due_date = models.DateField(null=True, blank=True)
    completed = models.BooleanField(default=False)
    completed_date = models.DateField(null=True, blank=True)
    created_by = models.ForeignKey(User, null=True, blank=True, related_name='usertask', on_delete=models.CASCADE)
    task_type = models.ForeignKey(TaskType,related_name='usertask', on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def over_due_status(self):   
        '''returns whether the task's due date has passed or not'''
        if self.due_date < datetime.date.today():
            return True
        else:
            return False
    
class Notification(BaseDateTime):
    notification_task = models.ForeignKey(Task,related_name='+', on_delete=models.CASCADE)
    title = models.CharField(max_length=50)
    description = models.TextField(null=True, blank=True)
    hyperlink = models.CharField(max_length=100, null=True, blank=True)

    def __str__(self):
        return self.title

