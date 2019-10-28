from django.urls import path
from todos import views

app_name = 'todos'
urlpatterns = [
    path('',views.index, name='index'),

    # 보여주는 new
    path('new/', views.new, name='new'),
    # 만드는 create
    path('create/', views.create, name='create'),

    path('add/', views.add, name='add'),

    path('<int:id>/delete/', views.delete, name="delete"),

    path('update/', views.update, name='update'),
]