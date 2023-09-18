from django.db import models


class Todo(models.Model):

    title = models.CharField(max_length=120)

    description = models.TextField(blank=True)

    created_time = models.DateTimeField(auto_now_add=True)

    updated_time = models.DateTimeField(auto_now=True)

    is_done = models.BooleanField(default=False)
 
    def __str__(self) -> str:
        return self.title