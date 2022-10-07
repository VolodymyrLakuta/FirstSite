from django.shortcuts import redirect, render
from .models import DishesCategory, Dish, Gallery
import random
from .forms import BookTableForm, UserMessageForm

def main_page_view(request):

    if request.method == "POST" and "btn_booktable" in request.POST:
        user_booktable = BookTableForm(request.POST)
        if user_booktable.is_valid():
            user_booktable.save()
            return redirect("/")
    
    if request.method == "POST" and "btn_usermsg" in request.POST:
        user_message = UserMessageForm(request.POST)
        if user_message.is_valid():
            user_message.save()
            return redirect("/")
            
    categories = DishesCategory.objects.filter(is_visible=True)
    dishes = Dish.objects.filter(is_visible=True)
    specialdishes = Dish.objects.filter(is_visible=True).filter(is_special=True)
    gallery = Gallery.objects.filter(is_visible=True)
    gallery = random.choices(gallery, k=8)
    user_booktable = BookTableForm()
    user_message = UserMessageForm()
    
    return render(request, 'main_page.html', context={
        'categories': categories,
        "dishes": dishes,
        "specialdishes": specialdishes,
        "gallery": gallery,
        "user_booktable": user_booktable,
        "user_message": user_message
    })

