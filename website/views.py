from django.shortcuts import render
from .models import Home, Benefit, Ingredient, Contact

# Create your views here.
def home(request):
    home_content = Home.objects.first()  # one main home record
    return render(request, 'index.html', {'home': home_content})


def benefits(request):
    benefits_list = Benefit.objects.all()
    return render(request, 'benefits.html', {'benefits': benefits_list})


def ingredients(request):
    ingredients_list = Ingredient.objects.all()
    return render(request, 'ingredients.html', {'ingredients': ingredients_list})


def contact(request):
    contact_info = Contact.objects.first()
    return render(request, 'contact.html', {'contact': contact_info})
