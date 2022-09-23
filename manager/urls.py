from django.urls import path
from .views import *

urlpatterns = [
    path('add/', add),
    path('delete/', delete),
    path('edit/', edit),
    
]