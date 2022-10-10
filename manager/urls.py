from django.urls import URLPattern, path
from .views import reservation_list

urlpatterns = [
    path('reservation/', reservation_list, )

]