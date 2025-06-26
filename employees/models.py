from django.db import models

# Create your models here.

# create a class Employee
class Employee(models.Model):
    emp_id = models.CharField(max_length=20)
    emp_name = models.CharField(max_length=100)
    designation = models.CharField(max_length=100)


    def __str__(self):
        return self.emp_name # this will reflecct in admin panel
 
