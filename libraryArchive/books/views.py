from django.shortcuts import render
from .models import Book

def books(request):
    books_list = Book.objects.all()
    context = {
        'books_list': books_list,
    }
    return render(request, 'books/books.html', context)
