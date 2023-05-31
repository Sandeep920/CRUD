from django.shortcuts import render,redirect
from .models import *

# Create your views here.
def Home(request):
    views = {}
    views['emp'] = Employees.objects.all()
    return render(request, 'index.html', views)

def ADD(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        data = Employees(
            name = name,
            email = email,
            address = address,
            phone = phone
        )
        data.save()
        return redirect('home')
    return render(request, 'index.html')

def EDIT(request):
    views = {}
    views['emp'] = Employees.objects.all()


    return redirect(request,'index.html',views)

def UPDATE(request,id):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        phone = request.POST.get('phone')

        data = Employees(
            id = id,
            name=name,
            email=email,
            address=address,
            phone=phone
        )
        data.save()
        return redirect('home')

    return redirect(request,'index.html')

def DELETE(request,id):
    views = {}
    views['emp'] = Employees.objects.filter(id = id).delete()
    return redirect('home')

