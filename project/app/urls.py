from django.urls import path
from . import views

urlpatterns = [
    path('',views.index),
    path('todo_update/<int:slno>',views.todo_update),
]
