from django.contrib import admin

# Register your models here.
from .models import Priority, Task

class TaskAdmin(admin.ModelAdmin):
    fieldsets=[
        ("General Information", {"fields":["title", "description"]}),
        ("Date Information", {"fields":["due_date"]})
    ]
    list_display=["title", "pub_date", "due_date","is_completed"]
    list_filter=["priorityLevel"]
    search_fields=["title"]

admin.site.register(Task, TaskAdmin) # this takse only the model and optionally the admin class
admin.site.register(Priority)