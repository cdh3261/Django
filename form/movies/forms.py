from django import forms
import datetime
from .models import Movie,Comment

class MovieForm(forms.Form):
    title = forms.CharField(max_length=100)
    title_en = forms.CharField(
                    max_length=100,
                    label="영문제목",
                    widget=forms.TextInput(
                        attrs={
                            'placeholder': '영문제목을 입력해주세요'
                        }
                    )
                )
    audience = forms.IntegerField()
    open_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    genre = forms.CharField(max_length=100)
    watch_grade = forms.CharField(max_length=100)
    score = forms.FloatField()
    poster_url = forms.CharField(widget=forms.Textarea)
    description = forms.CharField(widget=forms.Textarea)

class MovieModelForm(forms.ModelForm):
    open_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    class Meta:
        model = Movie
        fields = '__all__'


class CommentModelForm(forms.ModelForm):
    class Meta:
        model = Comment
        fields = ('content',)