from django.shortcuts import render, redirect
from django.views.decorators.http import require_POST

from .models import User
from .forms import UserForm

def index(request):

    form = UserForm()

    context = { 'form' : form}

    return render(request, 'user/index.html', context)
def lists(request):
    user_list = User.objects.order_by('id')

    form = UserForm()

    context = {'user_list' : user_list, 'form' : form}

    return render(request, 'user/lists.html', context)
def addForm(request):

    form = UserForm()

    context = {'form' : form}

    return render(request, 'user/add-form.html', context)
@require_POST
def addTodo(request):
    form = UserForm(request.POST)

    if form.is_valid():
        user = User(name = request.POST['name'],email=request.POST['email'])
        user.save()

    return redirect('index')
