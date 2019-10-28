from django import forms
from .models import Todo
class TodoForm(forms.ModelForm):
    due_date = forms.DateField(
        widget=forms.DateInput(attrs={'type':'date'})
    )
    # 어떤 정보와 연결되어있다.. 메타
    class Meta():
        model = Todo
        fields = ('content','due_date')