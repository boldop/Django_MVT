from django.shortcuts import render
from django.http import HttpResponse
from . models import *

# Create your views here.
def index(request):
    return HttpResponse("welocme bro.........")


def home(request):
    product = Product.objects.all()
    context = {
        "product":product,
    }
    return render(request, 'products/index.html', context)