from django.contrib import admin
from .models import *

# Register your models here.

class ToDoAdmin(admin.ModelAdmin):
    fields = ("name", "description", "priority", "date")
    date_hierarchy = "date"

class PriorityAdmin(admin.ModelAdmin):
    pass

admin.site.register(ToDo, ToDoAdmin)
admin.site.register(Priority, PriorityAdmin)
