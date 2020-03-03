from django.db import models
from authors.models import Author

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    language = models.CharField(max_length=15) # could be a list but kiss for now
    pages = models.IntegerField()
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.title
