from django.urls import path
from . import views

app_name = 'books'

urlpatterns = [
    path('', views.books, name='books'),
    path('<id>', views.book_by_id, name='book_by_id'),
]
