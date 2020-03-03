from django.db import models

class Author(models.Model):
    author_id = models.AutoField(primary_key=True)
    full_name = models.CharField(max_length=50, unique=True)
    # biography

    def __str__(self):
        return self.full_name
