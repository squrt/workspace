from django.db import models


# Create your models here.

class Employee(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Entry(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Blog(models.Model):
    name = models.CharField(max_length=30)
    entry = models.ForeignKey(Entry)

    def __str__(self):
        return self.name


sex_choices = (('f', 'female'), ('m', 'male'))


class User(models.Model):
    name = models.CharField(max_length=30)
    sex = models.CharField(max_length=1, choices=sex_choices)


class Author(models.Model):
    name = models.CharField(max_length=20)

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(max_length=20)
    authors = models.ManyToManyField(Author)

    def __str__(self):
        return self.name

    class Admin:
        list_display = ('name', 'authors',)
        list_filter = ('name', 'authors')
        ordering = ('-name',)
        search_fields = ('name',)


class ImgFile(models.Model):
    name = models.CharField(max_length=20)
    imgfile = models.FileField(upload_to='./upload/')

    def __str__(self):
        return self.name
