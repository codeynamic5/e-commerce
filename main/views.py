from django.shortcuts import render

# Create your views here.
def show_main(request):
    context = {
        'name' : 'matcha latte',
        'price': 'Rp22.000',
        'description': 'Matcha goodness'
    }

    return render(request, "main.html", context)