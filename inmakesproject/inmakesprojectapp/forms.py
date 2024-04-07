from django import forms
from . models import Movie,Review



class MovieForm(forms.ModelForm):
    class Meta:
        model=Movie
        fields=['title','description','category','poster','actors','link','added_by']



class ReviewForm(forms.ModelForm):
    class Meta:
        model = Review
        fields = ['rating', 'comment']



