from django.contrib import admin

# Register your models here.


from .models import Student

#thsi is how to register in admin panel 
admin.site.register(Student)