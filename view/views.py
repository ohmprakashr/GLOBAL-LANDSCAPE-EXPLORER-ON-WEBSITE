from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages


# Create your views here.
def home(request):
    return render(request,"view/index.html")

def about(request):
    return render(request,"view/about.html")

def collections(request):
    Collection=collection.objects.filter(status=0)
    return render(request,"view/collections.html",{"Collection":Collection} )

def collectionsview(request,name):
    if(collection.objects.filter(name=name,status=0)):
        Places=places.objects.filter(collections__name=name)
        return render(request,"places/index.html",{"Places":Places} )
    else:
        messages.warning(request,"No such collection Found")
        return redirect('collections')
