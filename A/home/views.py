from django.shortcuts import render, redirect
from django.views import View
from django.contrib import messages

from .forms import (
    TodoCreateForm, TodoUpdateForm, 
)

# local models
from .models import (
    Todo,
)

class HomeView(View):
    def get(self,request):
        return render(request, './home/home.html')
    

class TodoListView(View):

    def get(self, request):

        todos = Todo.objects.all()

        context = {'todos': todos}

        response = render(request, './home/todoList.html', context=context)

        return response
    

class TodoDetailView(View):

    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        return render(request, './home/todo-details.html', {'todo': todo})



def deleteTodo(request, id):
    Todo.objects.get(id=id).delete()
    messages.success(request, 'Todo deleted successfully!', 'success')
    return redirect(to='Todo-page')


class UpdateTodoView(View):

    def get(self, request, id):
        todo = Todo.objects.get(id=id)
        form = TodoUpdateForm(instance=todo)
        return render(request, './home/todoUpdate.html', {'form': form})

    def post(self, request, id):
        todo = Todo.objects.get(id=id)
        form = TodoUpdateForm(request.POST, instance=todo)
        if form.is_valid():
            form.save()
            messages.success(request, "Todo successfuly Updated", 'success')
            return redirect('Todo-detail', id)



class TodoCreateView(View):
    
    def post(self, request):
        form = TodoCreateForm(request.POST)
        if form.is_valid():
            cd = form.cleaned_data
            Todo.objects.create(title=cd['title'], description=cd['description'])
            messages.success(request, 'Todo created successfuly!', 'success')
            return redirect('Todo-page')

    def get(self, requeest):
        form = TodoCreateForm()
        return render(requeest, './home/todoCreate.html', {'form': form})
    


def doneTodo(request, id):
    todo = Todo.objects.get(pk=id)

    if todo.is_done:
        messages.warning(request, "This Todo is already done!", 'warning')
    else:
        todo.is_done = True

        todo.save()
        messages.success(request, 'Todo is Done!!', 'success')

    return render(request, './home/todo-details.html', {'todo': todo})


def update(request, id):
    todo = Todo.objects.get(id=id)
    pass
