from django.contrib import admin

from .models import Task


@admin.register(Task)
class Task(admin.ModelAdmin):
    list_display = ('name', 'description', 'created_at', 'is_completed', 'created_by')
