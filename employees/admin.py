from django.contrib import admin
from .models import Employee


# Register your models here.
admin.site.register(Employee)  # this will register the Employee model in admin panel
