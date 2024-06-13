from django.contrib import messages
from django.shortcuts import redirect, render
from .models import Friends
from django.views.decorators.csrf import csrf_protect

# Create your views here.
def home(request):
    users = Friends.objects.all()
    return render(request,'home.html',{'users':users})

def payment(request):
    users = Friends.objects.all()
    return render(request,'payment.html',{'users':users})

def transactions(request):
    users = Friends.objects.all()
    return render(request,'payment.html',{'users':users})

@csrf_protect
def add_user(request):
    name = request.POST.get("username")
    name_exist = Friends.objects.filter(username=name)
    if name_exist:
        messages.warning(request,"User already Exist.")
        return redirect('home')
    obj = Friends.objects.create(username=name)
    obj.save()
    messages.success(request,"User Added Successfully.")
    return redirect('home')
