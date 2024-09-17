from django.shortcuts import render, redirect
from main.forms import ProductEntryForm
from main.models import ProductEntry
from .models import Product

# Create your views here.
def show_main(request):
    product_entries = ProductEntry.objects.all()
    
    return render(request, "main.html")

def show_model_main(request):

    context = Product.objects.all()
    
    return render(request, "model_main.html", {'context' : context})

def show_static_main(request):
    return render(request, "static_main.html")

def create_product_entry(request):
    form = ProductEntryForm(request.POST or None)

    if form.is_valid and request.method == "POST":
        form.save()
        return redirect('main:show_main')
    
    context = {'form': form}
    return render(request, "create_product_entry.html", context)