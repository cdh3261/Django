from django.urls import path
from . import views

app_name = 'questions'

urlpatterns = [
    #'' 를 index 로 부르겠다.
    path('',views.index, name='index'),
    path('<int:id>/',views.detail, name='detail'),

    path('create/', views.create, name='create'),

    path('<int:question_id>/answers/',views.answer_create, name="answer_create"),
    path('<int:question_id>/answers/<int:answer_id>/delete',views.answer_delete, name="answer_delete")
]
