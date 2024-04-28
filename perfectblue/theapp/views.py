from django.shortcuts import render
from django.http import HttpRequest
from theapp.models import Destination
from theapp.models import Products
from theapp.models import PProducts 
from django.contrib import messages 

# Create your views here.
def first(request):
    results =Destination.objects.all()
    return render(request,'theapp/index.html',{"trdst":results}) 

def second(request):
    return render(request,'theapp/about.html') 

def third(request):
    return render(request,'theapp/contact.html')  

def items(request):
    results =Products.objects.all()
    return render(request, 'theapp/products.html',{"item":results}) 

def cpinsert(request,id):
      results= Products.objects.get(id=id)
      if request.method=="POST":
        if request.POST.get("cname") and request.POST.get("cadd") and request.POST.get("cmob"):
            obj= PProducts()
            obj.pcname=request.POST.get("cname") 
            obj.pcadd1=request.POST.get("cadd")
            obj.pcmobile= request.POST.get("cmob")
            obj.save()
            messages.success(request, "The Record " + obj.pcname + " Is saved succesfully")
            return render(request, "theapp/purchasing.html", {"item":results}  )
      else:
           return render(request, "theapp/purchasing.html", {"item":results}) 

def ppdisplay(request):
    results= PProducts.objects.all()
    return render(request, "theapp\pproducts.html", {"crudst":results} )