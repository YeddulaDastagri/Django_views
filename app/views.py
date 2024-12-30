from django.shortcuts import render 
from django.http import HttpResponse 
from app.models import *

# Create your views here. 

def insert_topic(request):
    tn=input("enter topicname") 
    tod=Topic.objects.get_or_create(topicname=tn) 
    if tod[1]: 
        LTO=Topic.objects.all() 
        d={'LTO':LTO} 

        return render(request,'display_topics.html',d) 

    else:
        return HttpResponse("given topic is already present")    


def insert_webpages(request):
    tn=input() 
    n=input() 
    url=input() 
    email=input() 
    LTO=Topic.objects.filter(topicname=tn)  
    if LTO:
        WTOD=WebPages.objects.get_or_create(topicname=LTO[0],name=n,urls=url,email=email)  
        if WTOD[1]:
            LWO=WebPages.objects.all() 
            d={'LWO':LWO}  

            return render(request,'display_webpages.html',d)
        else:
            return HttpResponse("wedpage is persent") 
    else:
        return HttpResponse("given topic is not present in database")    


def insert_access(request):  
    pk=int(input('enter of webpage')) 
    author=input('enter author') 
    date=input('enter date')  
    LWO=Webpages.objects.filter(pk=pk) 
    if LWO:
        ATOD=AccessRecords.objects.get_or_create(name=LWO[0],author=author,date=date) 
        if ATOD[1]: 
            LAO=AccessRecords.objects.all() 
            d={'LAO':LAO} 

            return render(request,'display_access.html',d)
        else:
            return HttpResponse('Given acess is present') 
    else:
        return HttpResponse('given parent webpage  table data is not present in database')       


def display_topics(request):
    LTO=Topic.objects.all() 
    d={'LTO':LTO} 

    return render(request,'display_topics.html',d) 

def display_webpages(request):
    LWO=WebPages.objects.all() 
    d={'LWO':LWO}  

    return render(request,'display_webpages.html',d)
def display_access(request):
    LAO=AccessRecords.objects.all() 
    d={'LAO':LAO} 

    return render(request,'display_access.html',d)


