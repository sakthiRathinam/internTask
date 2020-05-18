from django.shortcuts import render,redirect
from .models import *
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
# Create your views here.
from .serializers import *
from django.http import HttpResponse,JsonResponse
from rest_framework import status
from .forms import *
import json
from django.contrib import messages
import datetime
#this is the function for get all the users and their activity period
def users(request):
	l=[]
	for i in range(1,3):
		users=user.objects.get(id=i)
		l.append(users)
		activitys=users.activity_set.all()
		l.append(activitys)
	context={'l':l,}
	print(l)
	return render(request, 'html/index.html',context)
#this is the function to get the specific user and their activity period
def get_user(request,pk):
	userr=user.objects.get(id=pk)
	activitys=userr.activity_set.all()
	context={'user':userr,'activity':activitys}
	return render(request, 'html/index.html',context)
#this is the api to get all the users and their activity periods 
class UserModelViewSet(viewsets.ModelViewSet):
	serializer_class=ActivitySerializer
	queryset=Activity.objects.all()
#for user registration
def registerPage(request):
	form=UserForm()
	if request.method=='POST':
		form=UserForm(request.POST)
		if form.is_valid():
			user=form.save()
			username=form.cleaned_data.get('username')
			messages.success(request,"Account was created successfully" + username)
			return redirect('login')
	context={'form':form}
	return render(request,'html/register.html',context)
#for user login
def loginPage(request):
	if request.method=="POST":
		username=request.POST.get('username')
		password=request.POST.get('password')
		user=authenticate(request,username=username,password=password)
		if user is not None:
			login(request,user)
			return redirect('customerCreate')
		else:
			messages.info(request,'Username or password is incorrect')
	context={}
	return render(request,'html/login.html',context)
#for user logut
def logoutUser(request):
	logout(request)
	return redirect('login')