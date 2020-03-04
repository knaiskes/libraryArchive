from django.urls import path
from . import views

app_name = 'authors'

urlpatterns = [
    path('', views.authors, name='authors'),
    path('<id>', views.author_by_id, name='author_by_id'),
]
