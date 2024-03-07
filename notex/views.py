from django.shortcuts import render ,redirect
from django.http import HttpResponse
from django.template import loader
from . import models


def index(request):
    data=[]
    data2=[]
    template=loader.get_template('index.html')
    if request.method == 'POST':
            email=request.POST.get('emailname')
            passw=request.POST.get('logpassw')
            #simple increaption
            for i in email:
                increapt=ord(i)
                increapt+=5
                r=chr(increapt)
                data.append(r)
            emailin="".join(data)
            for i in passw:
                increapt=ord(i)
                increapt=increapt+19
                r=chr(increapt)
                data2.append(r)
            passin="".join(data2)
            userdt=models.Useridpas(email=emailin, password=passin)
            userdt.save()
    elif request.method == 'GET':
        try:
            username=request.GET.get('inputname')
            useremail=request.GET.get('inputemail')
            feedback=request.GET.get('feedback')
            user_feedback=models.feedback(name=username,email=useremail,feedback=feedback)   
            user_feedback.save()
        # except models.feedback.DoesNotExist:
        except Exception as e:
            # return HttpResponse('<body><h1 style="color:red">Error</h1><a href="login"><button style="width:80px;height:27px;">back</button></a></body>')                
            return HttpResponse(template.render()) 
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



def userlogin(request):
    current_path = request.path
    data=[]
    data2=[]
    template = loader.get_template('user.html')
    if request.method == 'POST':
        logusername = request.POST.get('logusername')
        logpassw = request.POST.get('logpassw')
        for i in logusername:
                increapt=ord(i)
                increapt+=5
                r=chr(increapt)
                data.append(r)
        lgemailin="".join(data)
        for i in logpassw:
            increapt=ord(i)
            increapt+=19
            r=chr(increapt)
            data2.append(r)
        lgpassin="".join(data2)
        try:
            user = models.Useridpas.objects.get(email=lgemailin)
            
            if user.password == lgpassin:
                return HttpResponse(template.render())
            else:
                return HttpResponse('<h1 style="color:red">Incorrect password</h1><br><a href="login"><button style="width:80px;height:27px;">back</button></a>')
        
        except models.Useridpas.DoesNotExist:
            return HttpResponse('<body><h1 style="color:red">User not found</h1><a href="login"><button style="width:80px;height:27px;">back</button></a></body>')
        
