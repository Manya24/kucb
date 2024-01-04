from django.shortcuts import redirect, render
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
# Create your views here.

def home(request):
    return render(request,'home.html',{'name':'home'})

def add(request):
    print("-----------------------------------------------")
    print(request)

    if request.method == 'POST':
        print(request.POST)
        print(request.POST.get('user'))
    return render(request,'loggedin.html')

def login(request):
    if request.method == 'POST':
        username =request.POST['username']
        password =request.POST['password'] 
        print(username,password)

        user =auth.authenticate(username=username,password=password)

        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.info(request,'invalid credentials')
            return redirect('home.html')

def register(request):
    if request.method == 'POST':
        First_name = request.POST['First_name']
        Last_name = request.POST['Last_name']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        
        username = request.POST['username']

        user = User.objects.create_user(username=username, first_name=First_name, last_name=Last_name, password=password1)
        user.save()

    return render(request, 'register.html')

def home(request):
    users = User.objects.all()
    return render(request, 'home.html', {'users': users})