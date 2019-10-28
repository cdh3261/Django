from django import forms
from .models import Post
class PostForm(forms.ModelForm):
    class Meta: # 연결시킬 정보를 준다.
        model = Post
        fields = ('title', 'content',)