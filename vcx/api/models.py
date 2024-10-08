from django.db import models

# Create your models here.


class Author(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)

    def __str__(self):
        return self.name


class Book(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, verbose_name="nome")
    edition = models.CharField(max_length=100, verbose_name="edição")
    year_published = models.IntegerField(verbose_name="ano de publicação")
    authors = models.ManyToManyField(
        Author, related_name="books"
    )  # django ja relaciona automaticamente, nome eh books para chamar
