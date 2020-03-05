from django.db import models

class Author(models.Model):
    full_name = models.CharField(max_length=80, unique=True)
    biography = models.TextField(max_length=700)

    def __str__(self):
        return self.full_name
