from django.shortcuts import HttpResponse

def hello(request, name):
    return HttpResponse(f"Hello, {name.title()}!")

def base(request):
    return HttpResponse("This is the first page of my site")