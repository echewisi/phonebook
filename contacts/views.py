from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout, get_user_model
from django.contrib import messages
from django.contrib.auth.models import AbstractUser
from .forms import IndividualForm



def homepage(request):
    return render(request, 'contacts/home.html')


def register_page(request):
    User= get_user_model
    form= IndividualForm
    if request.method == 'POST':
        form= IndividualForm(request.POST)
        if form.is_valid():
            form.save()
            login(request, User)
        else:
            return redirect('register')
    else:
        form= IndividualForm()
    context={'form':form}
    return render(request, 'contacts/register.html', context)



def login_page(request):
    if request.method== 'POST':
        username= request.POST.get('username').lower()
        password= request.POST.get('password').lower()

        try:
            user= AbstractUser.objects.get(username=username, password=password)
        except:
            messages.error(request, 'user does not exist')
        
        user= authenticate(username=username, password=password)
        if user is None:
            login(request, user)
            return redirect('home')        
    return render(request, 'contacts/login.html')

# Create your views here.
