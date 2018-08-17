from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('lists', views.lists, name='lists'),
    path('add-form', views.addForm, name="add-form"),
    path('add', views.addTodo, name='add'),
]
