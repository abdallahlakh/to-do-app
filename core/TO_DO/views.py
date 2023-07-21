from multiprocessing import AuthenticationError
from django.shortcuts import render,redirect
from django.urls import reverse_lazy
from .models import Mission
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import CreateView,UpdateView,DeleteView,FormView
from django.contrib.auth.views import LoginView
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.mixins import  LoginRequiredMixin
from django.contrib.auth import login
from django.shortcuts import render,redirect
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
# Create your views here.
def register(request):
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        password=request.POST['password']
        email= request.POST['email']  
        username= request.POST['username']      
        user=User.objects.create_user(first_name=first_name,last_name=last_name,password=password,email=email,username=username)
        user.is_superuser = True
        user.is_staff = True
        user.save()
        login(request, user)
        return redirect('/')
    else:
        return render(request, 'register.html')
   


def logining(request):
    if request.method=="GET":
        return render(request,'login.html')
    else:
        user=authenticate(request,username=request.POST['username'],password=request.POST['password'])
        login(request, user)
        return redirect('/')
        
def logouting(request):
    logout(request)
    return redirect('/')

            


@login_required
def show_mission_list(request):
    if request.user.is_authenticated:
       data = Mission.objects.filter(user=request.user)
    else:
       data=Mission.objects.none()   
    return render(request, 'mission_list.html', {'data': data})

def show_mission_detail(request, pk):
    data = Mission.objects.get(pk=pk)
    return render(request, 'mission_detail.html', {'data': data})

def mission_delete(request, pk):
    Mission.objects.get(pk=pk).delete()

    return redirect("/")




@login_required
def add_mission(request):
  if request.method=="GET":
       return render(request,'add_mission.html') 
  else :
      title=request.POST['titles']
      description=request.POST['descriptions']
      if 'complete' in request.POST:
        complete=True
      else:
        complete = False
      mission=Mission(title=title,description=description,complete=complete,user=request.user)
      mission.save()
      return redirect('/')
     
   

def mission_update(request, pk):
    if request.method=="GET":
       return render(request,'mission_update.html') 
    else :
      mission = Mission.objects.get(pk=pk)
      mission.title = request.POST['titles']
      mission.description = request.POST['descriptions']
      if 'complete' in request.POST:
        mission.complete = True
      else:
        mission.complete = False
      mission.save()
      return redirect('/')