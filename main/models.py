from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=100, default=None)
    nickname = models.CharField(max_length=100, blank=True)
    birth_date = models.DateField()

    def __str__(self):
        return self.name


class Book(models.Model):
    GENRE_CHOICES = [
        ('Fiction', 'Fiction'),
        ('Non-Fiction', 'Non-Fiction'),
        ('Mystery', 'Mystery'),
        ('Romance', 'Romance'),
        ('Science Fiction', 'Science Fiction'),
    ]
    title = models.CharField(max_length=200, default=None)
    genre = models.CharField(choices=GENRE_CHOICES, max_length=255, default=None)
    publication_date = models.DateField()
    author = models.ForeignKey(Author, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

