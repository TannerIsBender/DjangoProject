from django.shortcuts import render
from django.http import HttpResponse
import time
from .models import PageCounter

# Create your views here.

def index(request):
    
    row, create = PageCounter.objects.get_or_create(page='index')
    row.counter += 1
    row.save()
    
    return HttpResponse("Hello, you are visitor # " + str(row.counter) + "  || The time is: " + time.strftime("%c"))