from django.shortcuts import render
from django.http import HttpResponse
import random

# Create your views here.


def home(request):
    return render(request, "home.html")


def password(request):
    thepassword = "sholpinaabrakadabra" + str(random.randint(3, 333333))
    return render(request, "password.html", {"password": thepassword})
