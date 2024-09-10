from django.shortcuts import render
from django.http import HttpResponse
from .models import Product

# Create your views here.
def show_main(request):

    context = Product.objects.all()
    
    return render(request, "main.html", {'context' : context})