from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, unique=True)
    # biography

    def __str__(self):
        return self.full_name

class Tag(models.Model):
    name = models.CharField(max_length=20, unique=True)

    def __str__(self):
        return self.name

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    tags = models.ManyToManyField(Tag)

    title = models.CharField(max_length=50)
    publication_date = models.DateField()
    available = models.BooleanField()
    language = models.CharField(max_length=15) # could be a list but kiss for now
    pages = models.IntegerField()
    in_stock = models.BooleanField()
    description = models.TextField(max_length=150)

    def __str__(self):
        return self.title
