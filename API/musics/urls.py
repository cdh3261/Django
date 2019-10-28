from django.urls import path
from . import views

app_name = 'musics'

urlpatterns = [
    path('musics/', views.music_list, name='music_list'),
    path('musics/<int:id>/', views.music_detail, name='music_detail'),
]
