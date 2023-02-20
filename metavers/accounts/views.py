from django.contrib.auth import authenticate,login as authlogin ,logout as authlogout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
import MetaModel
from django.urls import reverse
from .forms import UserRegisterForm
from .forms import ProfileRegisterForm
from accounts.models import ProfileModel

# Create your views here.
def login(request):
    # post
    if request.method=='POST':
       username=request.POST.get('username')
       password=request.POST.get('password')
       user=authenticate(request,username=username,password=password)
       if user is not None:
            authlogin(request,user)
            # return HttpResponse("aa")
            # return HttpResponseRedirect('/meta/')
            return HttpResponseRedirect(reverse('MetaModel:home'))
            pass
       else:
        context={
            "username":username,
            "errorMessage":"Connect with wallet Not established or the password is wrong"
            }
        return render(request, "accounts/login.html",context) 
            # return render(request, "accounts/login.html",context)
    #get
    else:
     return render(request, "accounts/login.html",{})


def logout(request):
   authlogout(request)
#    return HttpResponse("aa")
   return render(request, "MetaModel/pages/home.html",)

def register(request):
       # post
    if request.method=='POST':
         form=UserRegisterForm(request.POST) 
         if form.is_valid():
            data = form.cleaned_data
            user=User.objects.create_user(username=data['User_Name'],email=data['Email'],
            password=data['Password'])
            user.save()

            profileModel=ProfileModel(user=user,Full_Name=data['Full_Name'],Password=data['Password'],Email=data['Email'])
            profileModel.save() 

            return render(request, "accounts/login.html",) 

    else:
         form=UserRegisterForm()

    context={
            'formData':form
         }
    return render(request, "accounts/register.html",context)



def profile(request):
    profile=request.user.profile
    context={
        'profile':profile
      }

    return render(request, "accounts/profile.html",context)



def profileRegister(request):
       # post
    
    if request.method=='POST':
       profileRegisterForm=ProfileRegisterForm(request.POST,request.FILES)
          
         # form=UserRegisterForm(request.POST) 
       if profileRegisterForm.is_valid():
            # data = form.cleaned_data
            user=User.objects.create_user(username=profileRegisterForm.cleaned_data["username"],
                              email=profileRegisterForm.cleaned_data['email'],
                              password=profileRegisterForm.cleaned_data['password'],
                              first_name=profileRegisterForm.cleaned_data['first_name'],
                              last_name=profileRegisterForm.cleaned_data['last_name'])
             
            user.save()
            profileModel=ProfileModel(user=user,ProfileImage=profileRegisterForm.cleaned_data['ProfileImage'],
                                          Full_Name=profileRegisterForm.cleaned_data['Full_Name'],
                                          Email=profileRegisterForm.cleaned_data['Email'])
            profileModel.save()                              
            return render(request, "accounts/login.html",) 

    else:
         profileRegisterForm=ProfileRegisterForm()

    context={
            'formData':profileRegisterForm
         }
    return render(request, "accounts/profileRegister.html",context)
