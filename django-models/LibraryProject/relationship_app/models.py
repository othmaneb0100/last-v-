from django.db import models

# Create your models here.
#Foreign key model
class Author(models.Model):
    name = models.CharField(max_length=100)

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='books')

class Library(models.Model):
    title = models.CharField(max_length=100)
    books = models.ManyToManyField(Book, on_delete=models.CASCADE, related_name='library')

class Librarian(models.Model):
    title = models.CharField(max_length=100)
    library = models.OneToOneField(Library, on_delete=models.CASCADE, related_name='librarian')

