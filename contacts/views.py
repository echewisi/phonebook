from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .serializers import ContactSerializer, IndividualSerializer
from rest_framework import status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
# from django.contrib.auth.models import AbstractUser

@api_view(['POST'])
@permission_classes([AllowAny])
def RegisterUser(request):
    if request.method== 'POST':
        serializer= IndividualSerializer(data=request.data)
        if serializer.is_valid():
            user=serializer.save()
        if user:
            return Response(serializer.data, status= status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status= status.HTTP_400_BAD_REQUEST)




# def homepage(request):
#     return render(request, 'contacts/home.html')


# def register_page(request):
#     form= SignupForm()
#     if request.method == 'POST':
#         form= SignupForm(request.POST)
#         if form.is_valid():
#             user=form.save()
#             user.username= user.username.lower()
#             user.password= user.password.lower()
#             login(request, user)
#             return redirect('home')
#         else:
#             return redirect('register')
#     else:
#         form= SignupForm()
#     context={'form':form}
#     return render(request, 'contacts/register.html', context)



# def login_page(request):
#     if request.method== 'POST':
#         username= request.POST.get('username').lower()
#         password= request.POST.get('password').lower()

#         try:
#             user= AbstractUser.objects.get(username=username, password=password)
#         except:
#             messages.error(request, 'user does not exist')
        
#         user= authenticate(username=username, password=password)
#         if user is None:
#             login(request, user)
#             return redirect('home')        
#     return render(request, 'contacts/login.html')

# Create your views here.
