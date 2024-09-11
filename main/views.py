from django.shortcuts import render
from .models import Product

# Create your views here.
def show_main(request):
    
    return render(request, "main.html")

def show_model_main(request):

    context = Product.objects.all()
    
    return render(request, "model_main.html", {'context' : context})

def show_static_main(request):
    return render(request, "static_main.html")