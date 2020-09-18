# Generated by Django 3.0.7 on 2020-09-18 03:11

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0009_auto_20200917_1332'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='generalRaiting',
            field=models.IntegerField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(max_length=255, unique=True, verbose_name='Title'),
        ),
        migrations.AlterField(
            model_name='raitingmovie',
            name='raiting',
            field=models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(5)]),
        ),
    ]