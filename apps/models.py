from django.db import models

class About(models.Model):
    describe = models.CharField(max_length=200)

class BookTable(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    date = models.DateField()
    time = models.TimeField()
    people_numb = models.IntegerField()
    message = models.CharField(max_length=100)

class Events(models.Model):
    title = models.CharField(max_length=20)
    describe = models.CharField(max_length=200)
    price = models.FloatField(max_length=6)

class Menu(models.Model):
    title = models.CharField(max_length=20)
    describe = models.CharField(max_length=200)
    price = models.FloatField(max_length=6)








