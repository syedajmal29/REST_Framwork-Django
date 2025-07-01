from django.shortcuts import render, get_object_or_404, redirect
from .models import Books, Review
from rest_framework import generics
from .serializers import BooksSerializer, ReviewSerializer




def book_list(request):
    books = Books.objects.all()
    return render(request, 'books.html', {'books': books})

def book_detail(request, pk):
    book = get_object_or_404(Books, pk=pk)
    reviews = book.reviews.all()

    if request.method == 'POST':
        comment = request.POST.get('comment')
        if comment:
            Review.objects.create(book=book, comment=comment)
            return redirect('book_detail', pk=pk)  # Correct: use redirect with URL name

    context = {
        'book': book,
        'reviews': reviews,
    }
    return render(request, 'book_detail.html', context)


class BooksListAPIView(generics.ListCreateAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer 


class BooksDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Books.objects.all()
    serializer_class = BooksSerializer



class ReviewListCreateAPIView(generics.ListCreateAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer


class ReviewDetailAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer

