from rest_framework import serializers
from students.models import Student 
from employees.models import Employee
from products.models import Product

class StudentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Student 
        fields = "__all__" #if we see say __all__ it means all the fields in student should be serialziers 
        

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Employee
        fields = '__all__'  # if we see say __all__ it means all the fields in employee should be serialziers


class ProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'  # if we see say __all__ it means all the fields in product should be serialziers     

        
           