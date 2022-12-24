from django.shortcuts import render, HttpResponse
from datetime import datetime
from home.models import Register
from django.contrib import messages


# Create your views here.
def index(request):
    return render(request,'index.html')
def about(request):
    return render(request,'about.html')
    
def movies(request):

    return render(request,'movies.html')
def forest(request):
    return render(request,'forest.html')    
def harry(request):
    return render(request,'harry.html')    
def inception(request):
    return render(request,'inception.html')    
def kgf(request):
    return render(request,'kgf.html')    
def doctor(request):
    return render(request,'doctor.html')    
def mission(request):
    return render(request,'mission.html')    
def frozen(request):
    return render(request,'frozen.html')    
def shrek(request):
    return render(request,'shrek.html')    
def scooby(request):
    return render(request,'scooby.html')    
    
def register(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        password = request.POST.get('password')
        phone = request.POST.get('phone')
        city = request.POST.get('city')
        state = request.POST.get('state')
        register = Register(name = name, email = email, password = password, phone = phone, city = city, state = state,date = datetime.today())
        register.save() 
        messages.success(request, 'Successfully Registered!')
    return render(request,'register.html') 
    

