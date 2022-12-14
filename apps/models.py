from django.db import models
import uuid
import os

class About(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    description = models.TextField(max_length=1000)
    photo = models.ImageField(upload_to=get_file_name)

    class Meta:
        verbose_name_plural = "About"

class Event(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    title = models.CharField(max_length=30)
    description = models.TextField(max_length=1000)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    position = models.SmallIntegerField()
    photo = models.ImageField(upload_to=get_file_name)

    def __str__(self):
        return f"({self.title}: {self.position}"

    class Meta:
        ordering = ("position", )


class DishesCategory(models.Model):
    title = models.CharField(max_length=30, unique=True)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField(unique=True)

    def __str__(self):
        return f"{self.title}: {self.position}"

    class Meta:
        verbose_name_plural = "Dishes Categories"
        ordering = ("position", )


class Dish(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/dishes/', filename)

    title = models.CharField(max_length=40, unique=True)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    is_special = models.BooleanField(default=False)
    is_visible = models.BooleanField(default=True)
    position = models.SmallIntegerField()
    ingredients = models.CharField(max_length=300)
    description = models.TextField(max_length=1000, blank=True)
    photo = models.ImageField(upload_to=get_file_name)
    category = models.ForeignKey(DishesCategory, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.category.title}: {self.title}: {self.position}"

    class Meta:
        verbose_name_plural = "Dishes"
        ordering = ("position", )

class Gallery(models.Model):

    def get_file_name(self, filename: str):
        ext = filename.strip().split('.')[-1]
        filename = f'{uuid.uuid4()}.{ext}'
        return os.path.join('images/gallery/', filename)

    photo = models.ImageField(upload_to=get_file_name)
    is_visible = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = "Galleries"
        










