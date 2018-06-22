from django.db import models

class Tasks(models.Model):
    task_id = models.IntegerField(default=0)
    completed = models.BooleanField(default=False)
    def __str__(self):
        return self.task_id
# Create your models here.
