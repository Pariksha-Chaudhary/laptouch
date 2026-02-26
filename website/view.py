from django.shortcuts import render
from .models import Service

def home(request):
    services = Service.objects.all()[:6]
    return render(request, "home.html", {"services": services})


def all_services(request):   # <-- MUST MATCH URL
    query = request.GET.get("q")

    if query:
        services = Service.objects.filter(name__icontains=query)
    else:
        services = Service.objects.all()

    return render(request, "all_services.html", {"services": services})

def about(request):
    return render(request, "about.html")