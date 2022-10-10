from django.shortcuts import render
from .models import BookTable

def reservation_list(request):
    lst = BookTable.objects.filter(is_processed=False)
    return render(request, 'reservation_list.html', context={'lst': lst})

