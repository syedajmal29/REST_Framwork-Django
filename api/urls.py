from django.urls import path, include
from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register('employees', views.EmployeeViewSet, basename='employee')  # Registering the EmployeeViewSet with the router

urlpatterns = [
    path('students/', views.studentsView), #to fetch all studnets
    path('students/<int:pk>/', views.studentDetailView),


    # path('employees/', views.Employees.as_view()),
      # this is cls-based view to fetch all employees
    # path('employees/<int:pk>/', views.EmployeeDetailView.as_view()),  # this is cls-based view to fetch a single employee by id  


    #path
    path('products/', views.Products.as_view()),  # to fetch all products
    path('products/<int:pk>/', views.ProductDetailView.as_view()),


    path('', include(router.urls)),
      # to include the router urls for EmployeeViewSet

   path('blogs/', views.BlogListView.as_view()),
        # to fetch all blogs
   path('comments/', views.CommentListView.as_view()),
        # to fetch all comments    
   path('blogs/<int:pk>/', views.BlogDeatilView.as_view()),

   path('comments/<int:pk>', views.CommentDetailView.as_view()),

   path('books/', views.Books.as_view()),  # to fetch all books
   path('books/<int:pk>/', views.BookDetailView.as_view()),  #

#    path('books/', views.booksView),
#    path('books/<int:pk>/', views.bookDetailView),  # to fetch a single book by id



]