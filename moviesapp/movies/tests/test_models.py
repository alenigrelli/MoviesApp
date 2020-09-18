from django.test import TestCase

from moviesapp.movies.models import Movie


class TestMovie(TestCase):

    def setUp(self):
        Movie.objects.create(
            pk='1',
            title='Guardians of the Galaxy Vol. 2',
            year='2019',
            rated='PG-13',
            released_on='2019-03-08',
            genre='Accion',
            director='Alejandro Nigrelli',
            plot='Esta entrega nos trae',
            created_at='2019-08-20T00:00:00+03:00',
            updated_at='2019-08-20T00:00:00+03:00'
        )

    def test_get_absolute_url(self):
        self.assertEqual(
            Movie.get_absolute_url(Movie.objects.get(pk=1)),
            '/movies/detail/1/' #estaba mal el path
        )

    def test_title(self):
        self.assertEqual(Movie.objects.get(pk=1).title, 'Guardians of the Galaxy Vol. 2')
