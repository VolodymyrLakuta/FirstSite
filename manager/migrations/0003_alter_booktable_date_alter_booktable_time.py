# Generated by Django 4.1.1 on 2022-10-05 06:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('manager', '0002_alter_booktable_options_remove_booktable_date_in'),
    ]

    operations = [
        migrations.AlterField(
            model_name='booktable',
            name='date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='booktable',
            name='time',
            field=models.TimeField(blank=True, null=True),
        ),
    ]