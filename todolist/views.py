from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib import messages
from urllib.parse import parse_qs
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import datetime
from django.http import HttpResponseRedirect, JsonResponse, HttpResponse
from django.urls import reverse
from todolist.models import *
from todolist.forms import *
from django.urls import reverse
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

@login_required(login_url='/todolist/login')
def show_todolist(request):

    tasks = Task.objects.filter(user=request.user)
    context = {
        'username_login': request.COOKIES['user_name'],
        'tasks': tasks
    }
    return render(request, 'todolist.html', context)


def register(request):
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,'Account has been created successfully!')
            return redirect('todolist:login')
    
    context = {'form':form}
    return render(request, 'register.html', context)

def login_user(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            response = redirect("todolist:show_todolist")
            response.set_cookie('last_login', str(datetime.datetime.now()))
            response.set_cookie('user_name', username)
            return response
        else:
            messages.info(request, 'Username or Password Incorrect!')
    context = {}
    return render(request, 'login.html', context)


def logout_user(request):
    logout(request)
    response = HttpResponseRedirect(reverse('todolist:login'))
    response.delete_cookie('last_login')
    response.delete_cookie('user_name')
    return response

def create_task(request):
    form = TaskForm(request.POST)
    if form.is_valid():
        task = form.save(commit=False)
        task.user = request.user
        task.save()
        return redirect('todolist:show_todolist')

    context = {
        'form': form
    }
    return render(request, 'create_task.html', context)

def delete_task(request, id):
    task = Task.objects.get(id = id)
    task.delete()
    return redirect('todolist:show_todolist')

def update_task(request, id):
    task = Task.objects.get(id = id)
    task.is_finished = not task.is_finished
    task.save()
    return redirect('todolist:show_todolist')

@login_required(login_url='/todolist/login')
def show_json(request):
    tasks = Task.objects.filter(user=request.user)
    return HttpResponse(serializers.serialize("json", tasks), content_type="application/json")
    
@login_required(login_url='/todolist/login')
def show_todo_json(request):
    tasks = Task.objects.filter(user=request.user)
    context = {
        'tasks' : tasks,
        'username': request.user,
    }
    return render(request, "todolist.html", context)

# https://stackoverflow.com/questions/51710145/what-is-csrf-exempt-in-django/51710363#51710363
@csrf_exempt
def add_task_modal(request):
    if request.method == "POST":
        title = request.POST.get("title")
        description = request.POST.get("description")
        date = datetime.date.today()
        task = Task.objects.create(user=request.user, title=title, description=description, date = date)

        data = {
            'fields': {
                'title': task.title,
                'description': task.description,
                'date': task.date,
            },
            'pk': task.pk
        }

        print(data)
        return JsonResponse(data)
