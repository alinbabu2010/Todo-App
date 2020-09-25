from django.db import models

class Todolist(models.Model):
    text = models.CharField(max_length=50)
    completed = models.BooleanField(default=False)

    def __str__(self):
        return self.text