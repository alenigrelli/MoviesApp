# -*- coding: utf-8 -*-
from django.urls import path

from . import views

app_name = 'movies'
urlpatterns = [
    path('', view=views.MovieListView.as_view(), name='index'),
    path('detail/<int:pk>/',view=views.MovieDetailView.as_view(), name='detail'),
    path('create/', view=views.MovieCreateView.as_view(), name='create'),
    path('rating/<int:pk>/', views.MovieRatingView.as_view(), name='rating'),
    path('update/<int:pk>/',
         view=views.MovieUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/',
         view=views.MovieDeleteView.as_view(), name='delete'),
]
