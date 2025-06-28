from django.contrib import admin
from .models import Book

# Register your models here.

admin.site.register(Book) # This will make the Book model available in the Django admin interface


