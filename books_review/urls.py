from django.urls import path
from . import views

urlpatterns = [

    #HTML Endpoints
    path('', views.book_list, name='book_list'),
    path('book/<int:pk>/', views.book_detail, name='book_detail'),


    #API Endpoints
    path('api/books/', views.BooksListAPIView.as_view(), name='books_list_api'),
    path('api/books/<int:pk>/', views.BooksDetailAPIView.as_view(), name='books_detail_api'),
    path('api/reviews/', views.ReviewListCreateAPIView.as_view(), name='reviews_list_api'),
    path('api/reviews/<int:pk>/', views.ReviewDetailAPIView.as_view(), name='reviews_detail_api'),
]