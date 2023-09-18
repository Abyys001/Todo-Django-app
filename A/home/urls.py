# local app urls

from django.urls import path

# local app views
from .views import (
    TodoListView,TodoDetailView,deleteTodo,TodoCreateView, doneTodo,
    UpdateTodoView, 
)

urlpatterns = [

    path('', TodoListView.as_view(), name='Todo-page'),

    path('TodoDetail/<int:id>/', TodoDetailView.as_view(), name='Todo-detail'),

    path('TodoDetail/<int:id>/done/', doneTodo, name="done-todo"),

    path('TodoDetail/<int:id>/delete/',deleteTodo, name='delete-todo'),

    path('Update/<int:id>/', UpdateTodoView.as_view(), name='update'),
    
    path('create/', TodoCreateView.as_view(), name='create'),

    
] 