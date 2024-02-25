from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from . import models


def index(request):
    template=loader.get_template('index.html')
    if request.method == 'POST':
            email=request.POST.get('emailname')
            passw=request.POST.get('logpassw')
            userdt=models.Useridpas(email=email, password=passw)
            userdt.save()            
    return HttpResponse(template.render())


def about(request):
    current_path = request.path
    template=loader.get_template('about.html')
    return HttpResponse(template.render({'current_path': current_path}, request))


def contact(request):
    previous_page = request.META.get('HTTP_REFERER', '/')
    current_path = request.path
    if request.method == 'POST':
        username=request.POST.get('inputname')
        useremail=request.POST.get('inputemail')
        feedback=request.POST.get('feedback')
        user_feedback=models.feedback(name=username,email=useremail,feedback=feedback)
        user_feedback.save()
    template=loader.get_template('contacts.html')
    return HttpResponse(template.render({'current_path': current_path,'previous_page': previous_page}, request))

def login(request):
    previous_page = request.META.get('HTTP_REFERER', '/')
    current_path = request.path 
    template=loader.get_template('login.html')
    return HttpResponse(template.render({'current_path': current_path,'previous_page': previous_page}, request))

def sign(request):
    previous_page = request.META.get('HTTP_REFERER', '/')
    current_path = request.path
    template=loader.get_template('signin.html')
    return HttpResponse(template.render({'current_path': current_path,'previous_page': previous_page}, request))

# def my_view(request):
#     if request.method == 'POST':
#         logusername=request.POST.get('logusername')
#         logpassw=request.POST.get('logpassw')
#         database=models.Useridpas
#         if logusername in database:
#             if database[logusername]==logpassw:
#                 return HttpResponse('successfully login')
#             else:
#                 return HttpResponse('Incorrect password')
#         else:
#             return HttpResponse("user not found")
        
#     current_path=request.path
#     template=loader.get_template('test.html')
#     return HttpResponse(template.render({'current_path': current_path}))


def userlogin(request):
    current_path = request.path
    template = loader.get_template('user.html')
    if request.method == 'POST':
        logusername = request.POST.get('logusername')
        logpassw = request.POST.get('logpassw')
        try:
            user = models.Useridpas.objects.get(email=logusername)
            
            if user.password == logpassw:
                return HttpResponse(template.render())
            else:
                return HttpResponse('<h1 style="color:red">Incorrect password</h1><br><a href="login"><button style="width:80px;height:27px;">back</button></a>')
        
        except models.Useridpas.DoesNotExist:
            return HttpResponse('<body><h1 style="color:red">User not found</h1><a href="login"><button style="width:80px;height:27px;">back</button></a></body>')
