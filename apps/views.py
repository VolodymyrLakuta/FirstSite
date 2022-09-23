from django.shortcuts import render, HttpResponse

def apps(request):
    return HttpResponse(f"apps are creating")

