# from django.shortcuts import render
# from django.http import JsonResponse
from students.models import Student
from products.models import Product
from books.models import Book
from .serializers import StudentSerializer, EmployeeSerializer, ProductSerializer, BookSerializer #we need to import what we created in serialziers 
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.views import APIView
from employees.models import Employee
from django.http import Http404
from django.shortcuts import get_object_or_404
from rest_framework import mixins , generics, viewsets  #if we want to use viewsets
from blogs.models import Blog, Comment
from blogs.serializers import BlogSerializer, CommentSerializer
from .paginations import CustomPagination  #if we want to use custom pagination
from employees.filters import EmployeeFilter  #if we want to use filters
from rest_framework.filters import SearchFilter





# from django.http import JsonResponse  #if we want to use JsonResponse

# from rest_framework import viewsets  #if we want to use viewsets


# Create your views here.



#this is manual serialzier but we should not follw this

    # students = Student.objects.all()
    # # print(students)
    # students_list = list(students.values())
    # return JsonResponse(students_list, safe=False)

# def productsView(request):
#     products = Product.objects.all()
#     products_list = list(products.values())
#     return JsonResponse(products_list, safe=False) 
# this is manual serialzier but we should not follw this
@api_view(['GET', 'POST'])    
def booksView(request):
    if request.method == 'GET':
        books = Book.objects.all()
        serializer = BookSerializer(books, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    elif request.method == 'POST':
        serializer = BookSerializer(data = request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['GET', 'PUT', 'DELETE'])    
def bookDetailView(request, pk):
    try:
        book = Book.objects.get(pk=pk)
    except Book.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = BookSerializer(book)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = BookSerializer(book, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        book.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        


    
    
             
           

    #function based views 
@api_view(['GET','POST', ])  #need to pass  
def studentsView(request): # function based views
    if request.method == 'GET':
        students = Student.objects.all()
        serializer = StudentSerializer(students, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        serializer = StudentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST )
    
@api_view(['GET', 'PUT', 'DELETE'])
def studentDetailView(request, pk):
    try:
        student = Student.objects.get(pk=pk)
    except Student.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == 'GET':
        serializer = StudentSerializer(student)
        return Response(serializer.data, status=status.HTTP_200_OK)
    elif request.method == 'PUT':
        serializer = StudentSerializer(student, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'DELETE':
        student.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)  
    

class Products(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
class ProductDetailView(APIView):
    def get_object(self, pk):
        try:
            product = Product.objects.get(pk=pk)
            return product
        except Product.DoesNotExist:
            raise Http404
    def get(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    def put(self, request, pk):
        product = self.get_object(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  
    def delete(self, request, pk):
        product = self.get_object(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT) 
    

 #class based views
 #    
# class Books(APIView):
#        def get(self, request):
#         books = Book.objects.all()
#         serializer = BookSerializer(books, many=True)
#         return Response(serializer.data, status=status.HTTP_200_OK) 
       
#        def post(self, request):
#            serializer = BookSerializer(data.request.data)
#            if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
       
# class BookDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             book = Book.objects.get(pk=pk)
#             return book
#         except Book.DoesNotExist:
#             raise Http404
#     def get(self, request, pk):
#             book = self.get_object(pk)
#             serializer = BookSerializer(book)
#             return Response(serializer.data, status=status.HTTP_200_OK)
#     def put(self, request, pk):
#         book = self.get_object(pk)
#         serializer = BookSerializer(book, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
#     def delete(self, request, pk):
#         book = self.get_object(pk)
#         book.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)  

    # # class based views
# class Employees(APIView):
#     def get(self, request):
#        employees = Employee.objects.all()
#        serializer = EmployeeSerializer(employees, many=True)
#        return Response(serializer.data, status=status.HTTP_200_OK)
    
#     def post(self, request):
#         serializer = EmployeeSerializer(data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_201_CREATED)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    
# class EmployeeDetailView(APIView):
#     def get_object(self, pk):
#         try:
#             employee = Employee.objects.get(pk=pk)
#             return employee
#         except Employee.DoesNotExist:
#             raise Http404

#     def get(self,request, pk): 
#         employee = self.get_object(pk)  
#         serializer = EmployeeSerializer(employee)
#         return Response(serializer.data, status=status.HTTP_200_OK) 

#     def put(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         if serializer.is_valid():
#             serializer.save()
#             return Response(serializer.data, status=status.HTTP_200_OK)
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     def delete(self, request, pk):
#         employee = self.get_object(pk)
#         serializer = EmployeeSerializer(employee, data=request.data)
#         employee.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT) 

  
# class Books(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     def get(self, request):
#         return self.list(request)
#     def post(self, request):
#         return self.create(request)
    
# class BookDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Book.objects.all()
#     serializer_class = BookSerializer
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#     def put(self,request, pk):
#         return self.update(request , pk)
#     def delete(self, request, pk):
#         return self.destroy(request, pk)    





   #mixins aviews
# class Employees(mixins.ListModelMixin, mixins.CreateModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer

#     def get(self, request):
#         return self.list(request)
    
#     def post(self, request):
#         return self.create(request)
    
# class EmployeeDetailView(mixins.RetrieveModelMixin, mixins.UpdateModelMixin, mixins.DestroyModelMixin, generics.GenericAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     def get(self, request, pk):
#         return self.retrieve(request, pk)
#     def put(self,request, pk):
#         return self.update(request , pk)
#     def delete(self, request, pk):
#         return self.destroy(request, pk)
    
    #generic views 
# class Employees(generics.ListCreateAPIView):
#     queryset = Employee.objects.all() #ORM
#     serializer_class = EmployeeSerializer  #this is the serializer we created in serializers.py

class Books(generics.ListCreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer  #this is the serializer we created in serializers.py


class BookDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    lookup_field = 'pk'  # this is the primary key field we are using to retrieve the book

    

# class EmployeeDetailView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Employee.objects.all()
#     serializer_class = EmployeeSerializer
#     lookup_field = 'pk'  # this is the primary key field we are using to retrieve the employee





class EmployeeViewSet(viewsets.ViewSet):
    def list(self,request):
        queryset = Employee.objects.all()
        serializer = EmployeeSerializer(queryset, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)
    
    def create(self, request):
        serializer = EmployeeSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def retrieve(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee)
        return Response(serializer.data, status=status.HTTP_200_OK) 
    def update(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        serializer = EmployeeSerializer(employee, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    def destroy(self, request, pk=None):
        employee = get_object_or_404(Employee, pk=pk)
        employee.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    
class EmployeeViewSet(viewsets.ModelViewSet):
    queryset = Employee.objects.all()
    serializer_class = EmployeeSerializer
    pagination_class = CustomPagination  #if we want to use custom pagination
      # this is the primary key field we are using to retrieve the employee
    # filterset_fields =['designation'] # this is global filter it works with exact field name
    filterset_class = EmployeeFilter  #if we want to use filters


    
class BlogListView(generics.ListCreateAPIView):
        queryset = Blog.objects.all()
        serializer_class = BlogSerializer
        filter_backends = [SearchFilter]  #if we want to use search filter
        search_fields =['blog_title']  #if we want to use search filter

class CommentListView(generics.ListCreateAPIView):
        queryset = Comment.objects.all()
        serializer_class = CommentSerializer  

class BlogDeatilView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer
    lookup_field = 'pk'

      
    
class CommentDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Comment.objects.all()
    serializer_class = CommentSerializer
    lookup_field = 'pk'


     #if we want to use custom pagination
      # this is the primary key field we are using to retrieve the employee

      #if we want to use custom pagination
      # this is the primary key field we are using to retrieve the employee

    





 




      
     

        
        


    
    