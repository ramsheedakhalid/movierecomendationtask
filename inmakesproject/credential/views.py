from django.contrib import messages,auth
from django.contrib.auth.models import User
from django.shortcuts import render,redirect
from .forms import RegisterForm



# Create your views here.
def loginuser(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']
        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request,user)
            return redirect('/')
        else:
            messages.info(request,"invalid credential")
            return redirect('/credential/loginuser')

    return render(request,"login.html")




def registerationn(request):
    if request.method=='POST':
        username=request.POST['username']
        first_name=request.POST['firstname']
        last_name=request.POST['lastname']
        email=request.POST['email']
        password=request.POST['password']
        cpassword=request.POST['password1']
        if password==cpassword:
            if User.objects.filter(username=username).exists():
                messages.info(request,"username taken")
            elif User.objects.filter(email=email).exists():
                messages.info(request,"email taken")
                return redirect('/credential/registerationn')
            else:
                user=User.objects.create_user(username=username,first_name=first_name,last_name=last_name,email=email,password=password)
                user.save();

        else:
            messages.info(request,"password not matching")
            return redirect('/credential/registerationn')
        messages.info(request, "registered successfully")
        return redirect('/credential/registerationn')
    return render(request,"register.html")

def logout(request):
    auth.logout(request)
    return redirect('/')



def display_user(request, username_id):
    user= User.objects.get(id=username_id)
    return render(request, 'profile.html', {'user': user})


def update_profile(request,username_id):
    user=User.objects.get(id=username_id)
    form=RegisterForm(request.POST or None,request.FILES,instance=user)
    if form.is_valid():
        form.save()
        return redirect('/')
    return render(request,'editprofile.html',{'form':form,'user':user})


def delete_profile(request,username_id):
    if request.method=='POST':
       user=User.objects.get(id=username_id)
       user.delete()
       return redirect('/')
    return render(request,'deleteprofile.html')

