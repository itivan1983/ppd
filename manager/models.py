from django.db import models

# Create your models here.
class Book(models.Model):

    class Mate:
        verbose_name = 'книга'
        verbose_name_plural = 'книги'

    title = models.CharField(max_length=100, verbose_name='название книги')