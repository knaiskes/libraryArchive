from django.shortcuts import render, get_object_or_404
from .models import Book

def books(request):
    books_list = Book.objects.all()
    context = {
        'books_list': books_list,
    }
    return render(request, 'books/books.html', context)

def book_by_id(request, id):
    book = get_object_or_404(Book, id=id)
    context = {
        'book': book,
    }
    return render(request, 'books/book.html', context)
