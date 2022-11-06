from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    mylist = [x for x in range(1, 10)]
    return render(request, "home.html", {"password": mylist})


def password(request):
    # thepassword = ({"id": random.randint(0, x), "name": f"Sholpan {x}", "age": x + 20} for x in range(1, 100)
    thepassword = "sholpinaabrakadabra" + str(random.randint(3, 333))
    return render(request, "password.html", {"password": thepassword})
