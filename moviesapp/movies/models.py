# -*- coding: utf-8 -*-
from django.urls import reverse
from django.core.validators import RegexValidator, MinValueValidator, MaxValueValidator
from django.db import models
from django.utils.translation import ugettext_lazy as _


class Movie(models.Model):
    title = models.CharField(_('Title'), max_length=255, unique=True)
    year = models.PositiveIntegerField(default=2019)
    # Example: PG-13
    rated = models.CharField(max_length=64)
    released_on = models.DateField(_('Release Date'))
    genre = models.CharField(max_length=255)
    director = models.CharField(max_length=255)
    plot = models.TextField(blank=True, null=True)
    generalRating = models.FloatField(default=0, null=True)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True) #averiguar para que el form acepte campos editables false
    # Todo: add Rating models

    def get_absolute_url(self):
        return reverse('movies:detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.title

class RatingMovie(models.Model):
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(5)])
    comment = models.CharField(max_length=1024, null=True)
    movie = models.ForeignKey(Movie, on_delete = models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)
    updated_at = models.DateTimeField(auto_now=True, editable=True) #averiguar para que el form acepte campos editables false