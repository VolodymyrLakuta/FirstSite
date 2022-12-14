# Generated by Django 4.1.1 on 2022-09-24 18:45

import apps.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('description', models.TextField(max_length=1000)),
                ('photo', models.ImageField(upload_to=apps.models.About.get_file_name)),
            ],
        ),
        migrations.CreateModel(
            name='BookTable',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('email', models.EmailField(max_length=254)),
                ('phone', models.CharField(max_length=20)),
                ('date', models.DateField()),
                ('time', models.TimeField()),
                ('people_numb', models.SmallIntegerField()),
                ('message', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DishesCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30, unique=True)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField(unique=True)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('description', models.TextField(max_length=1000)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('position', models.SmallIntegerField()),
                ('photo', models.ImageField(upload_to=apps.models.Event.get_file_name)),
            ],
            options={
                'ordering': ('position',),
            },
        ),
        migrations.CreateModel(
            name='Dish',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=40, unique=True)),
                ('price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('is_special', models.BooleanField(default=False)),
                ('is_visible', models.BooleanField(default=True)),
                ('position', models.SmallIntegerField()),
                ('ingredients', models.CharField(max_length=300)),
                ('description', models.TextField(blank=True, max_length=1000)),
                ('photo', models.ImageField(upload_to=apps.models.Dish.get_file_name)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='apps.dishescategory')),
            ],
            options={
                'ordering': ('position',),
            },
        ),
    ]
