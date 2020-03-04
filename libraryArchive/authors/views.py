from django.shortcuts import render, get_object_or_404
from .models import Author
from books.models import Book

def authors(request):
    authors_list = Author.objects.all()
    context = {
        'authors_list': authors_list,
    }
    return render(request, 'authors/authors.html', context)

def author_by_id(request, id):
    author = get_object_or_404(Author, id=id)
    books_list = Book.objects.filter(author=author)
    context = {
        'author': author,
        'books_list': books_list,
    }
    return render(request, 'authors/author.html', context)
