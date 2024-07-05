from django.shortcuts import render,redirect

# Create your views here.

#Written codes by ourself->
import random
from django.http import HttpResponse

# for email->
from .utils import send_email_to_client
from .models import *

# def home(request):
#     return HttpResponse("<h1>Hello World Server!</h1>")

text="""
The multiverse is the hypothetical set of all universes.[a] Together, these universes are
presumed to comprise everything that exists: the entirety of space, time, matter, energy, 
information, and the physical laws and constants that describe them. The different universes
within the multiverse are called "parallel universes", "flat universes", "other universes",
"alternate universes", "multiple universes", "plane universes", "parent and child universes",
"many universes", or "many worlds". One common assumption is that the multiverse is a 
"patchwork quilt of separate universes all bound by the same laws of physics."

The concept of multiple universes, or a multiverse, has been discussed throughout history,
including Greek philosophy. It has evolved over time and has been debated in various fields,
including cosmology, physics, and philosophy. Some physicists argue that the multiverse is a
philosophical notion rather than a scientific hypothesis, as it cannot be empirically falsified.
In recent years, there have been proponents and skeptics of multiverse theories within the 
physics community. Although some scientists have analyzed data in search of evidence for other
universes, no statistically significant evidence has been found. Critics argue that the multiverse
concept lacks testability and falsifiability, which are essential for scientific inquiry, 
and that it raises unresolved metaphysical issues.
         """
vegetables=["potato","tomato","brinjal","palak"]

def home(request):
    Car.objects.create(car_name=f"Nexon-{random.randint(0,100)}")

    peoples=[
        {"name":"P.T.","age":21},
        {"name":"Sriram","age":18},
        {"name":"Srikrishna","age":23},
        {"name":"Bhole","age":25},
        {"name":"Ganesha","age":24},
        {"name":"Hare","age":16},
        {"name":"kanha","age":17}

    ]
    # In below code,context helps to send data to html template...
    return render(request,'index.html',context={'peoples':peoples})

def about(request):
    return render(request,'about.html',context={'text':text,'vegetables':vegetables})

def contact(request):
    return render(request,'contact.html')


def send_email(request):
    send_email_to_client()
    return redirect('/')