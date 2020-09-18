from django import forms
from moviesapp.movies.models import Movie, RatingMovie
import datetime


class MovieForm(forms.ModelForm):

	class Meta:
		model = Movie

		fields = [
			'title',
    		'year',    
    		'rated',
    		'released_on',
    		'genre',
    		'director',
    		'plot',
		]
		labels = {
			'title' : 'title',
    		'year' : 'year',    
    		'rated' : 'rated',
    		'released_on' : 'released_on',
    		'genre' : 'genre',
    		'director' : 'director',
    		'plot' : 'plot',
		}
		widgets = {
			'title' : forms.TextInput(attrs={'class':'form-control'}),
    		'year' :  forms.TextInput(attrs={'class':'form-control'}),    
    		'rated' : forms.TextInput(attrs={'class':'form-control'}),
    		'released_on' :forms.DateInput(attrs={'class':'datetime-input'}),
    		'genre' : forms.TextInput(attrs={'class':'form-control'}),
    		'director' : forms.TextInput(attrs={'class':'form-control'}),
    		'plot' : forms.TextInput(attrs={'class':'form-control'}),
		}
class RatingForm(forms.ModelForm):

    class Meta:
        model = RatingMovie

        fields = [
            'rating',
            'comment',
        ]
        labels = {
            'rating' : 'your rating',
            'comment' : 'your comment',
        }
        widgets = {
            'rating' : forms.TextInput(attrs={'min': '1','max': '5','type': 'number','class':'form-control'}),
            'comment' : forms.TextInput(attrs={'class':'form-control'}),
        }