# -*- coding: utf-8 -*-

"""Movies views."""

from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView, View
from django.contrib import messages
from django.shortcuts import redirect, render 
from django.http import Http404
from django.urls import reverse_lazy 
from django.db.models import Sum

from .models import Movie, RatingMovie
from moviesapp.movies.forms import MovieForm, RatingForm
from django.views.generic.edit import FormView


class MovieListView(ListView):
	"""Show all movies."""
	model = Movie
	template_name = 'movies/movie_list.html'
	ordering = ['-generalRating','-year']
	def get_queryset(self):
		queryset = super().get_queryset()
		title = self.request.GET.get('Search')
		if title:
			return Movie.objects.filter(title=title)
		return queryset

class MovieDetailView(DetailView):
	"""Show the requested movie."""
	model = Movie
	template_name =  'movies/movie_detail.html'

	def get_context_data(self, **kwargs):
		context = super(MovieDetailView, self).get_context_data(**kwargs)
		context['form'] = RatingForm
		return context

class MovieCreateView(CreateView):
	"""Create a new movie."""
	model = Movie
	form_class = MovieForm
	template_name =  'movies/movie_form.html'
	success_url = reverse_lazy('movies:index')

class MovieUpdateView(UpdateView):
	"""Update the requested movie."""
	model = Movie
	form_class = MovieForm
	template_name =  'movies/movie_form.html'
	success_url = reverse_lazy('movies:index')

class MovieDeleteView(DeleteView):
	"""Delete the requested movie."""
	model = Movie
	template_name = 'movies/movie_confirm_delete.html'
	success_url = reverse_lazy('movies:index')

class MovieRatingView(FormView):
	form_class = RatingForm
	success_url = reverse_lazy('movies:index')

	def post(self, request, pk):
		#create Rating
		ratingvalue = request.POST['rating']
		commentvalue = request.POST['comment']

		ratings = RatingMovie.objects.filter(movie=Movie.objects.get(pk=pk)).count()
		RatingMovie.objects.create(rating=ratingvalue, comment=commentvalue, movie=Movie.objects.get(pk=pk))

		movierating = RatingMovie.objects.filter(movie=Movie.objects.get(pk=pk)).aggregate(Sum('rating'))
		ratingprom = round(float(movierating['rating__sum']) / (float(ratings)+1),1)	
		
		#update rating general
		movie = Movie.objects.filter(pk=pk)
		movie.update(generalRating=ratingprom)
		#import ipdb;ipdb.set_trace()
		return super().post(request)
