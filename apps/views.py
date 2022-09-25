from django.shortcuts import render, HttpResponse
from .models import DishesCategory, Dish

def main_page_view(request):

    categories = DishesCategory.objects.filter(is_visible=True)
    
    return render(request, 'main_page.html', context={
        'categories': categories,
    })

