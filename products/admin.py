from django.contrib import admin
from .models import Product

# Register your models here.
admin.site.register(Product)  # this will register the Product model in admin panel
