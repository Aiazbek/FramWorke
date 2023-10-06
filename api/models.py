from django.db import models
from django.contrib.auth.models import User


class Task(models.Model):
    name = models.CharField('Название задачи', max_length=255)
    description = models.TextField('Описание задачи')
    created_at = models.DateTimeField('Дата создания', auto_now_add=True)
    is_completed = models.BooleanField(default=False)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
