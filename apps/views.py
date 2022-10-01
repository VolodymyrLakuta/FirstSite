from django.shortcuts import render, HttpResponse
from .models import DishesCategory, Dish, Gallery
import random
from .forms import BookTableForm

def main_page_view(request):

    categories = DishesCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specialdishes = Dish.objects.filter(is_visible=True).filter(is_special=True)
    gallery = Gallery.objects.filter(is_visible=True)
    gallery = random.choices(gallery, k=8)
    user_booktable = BookTableForm()
    
    return render(request, 'main_page.html', context={
        'categories': categories,
        "dishes": dishes,
        "specialdishes": specialdishes,
        "gallery": gallery,
        "user_booktable": user_booktable,
    })

