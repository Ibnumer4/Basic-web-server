from django.db import models

# Create your models here.


class Book(models.Model):
    title = models.CharField(max_length = 2000)
    author = models.CharField(max_length = 500)
    isbn = models.CharField(max_length = 13, unique=True)
    published_year = models.IntegerField()
    is_favorite = models.BooleanField(default = False)  # For custom endpoint

    def __str__(self):
        return self.title
    
    