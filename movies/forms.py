from django import forms
from movies.models import Movie, Review

class MovieForm(forms.ModelForm):
    class Meta:
        model = Movie
        fields = ['title', 'description', 'release_date', 'genre', 'image']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'description': forms.Textarea(attrs={'class': 'form-control'}),
            'release_date': forms.DateInput(
                attrs={'class': 'form-control datetimepicker', 'type': 'date'},
                format='%Y-%m-%d'
            ),
            'genre': forms.Select(attrs={'class': 'form-control'}),
            'image': forms.ClearableFileInput(
                attrs={'class': 'form-control', 'accept': 'image/jpeg, image/png'}
            ),
        }

class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['autor', 'rating', 'comments']
        widgets = {
            'autor': forms.TextInput(attrs={'class': 'form-control'}),
            'rating': forms.Select(attrs={'class': 'form-control'}),
            'comments': forms.Textarea(attrs={'class': 'form-control'}),
        }
