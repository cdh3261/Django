from django.urls import path
from . import views

urlpatterns = [
    path('', views.index),  # ''을 받으면 views에서 index를 보여준다.

    path('new/', views.new),
    path('create/', views.create),

    path('<int:id>/delete/', views.delete),

    path('<int:id>/edit/', views.edit),
    path('<int:id>/update/', views.update),
]
