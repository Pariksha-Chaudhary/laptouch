from django.shortcuts import render,get_object_or_404 , redirect
from .models import Service, Laptop , Review


def home(request):

    if request.method == "POST":
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        if name and rating and comment:
            Review.objects.create(
                name=name,
                rating=int(rating),
                comment=comment
            )
        return redirect("home")

    services = Service.objects.all()[:6]
    laptops = Laptop.objects.filter(is_available=True).order_by('-created_at')[:6]
    reviews = Review.objects.filter(is_approved=True).order_by("-created_at")[:6]

    context = {
        "services": services,
        "laptops": laptops,
        "reviews": reviews,
    }

    return render(request, "home.html", context)


def all_services(request):   # <-- MUST MATCH URL
    query = request.GET.get("q")

    if query:
        services = Service.objects.filter(name__icontains=query)
    else:
        services = Service.objects.all()

    return render(request, "all_services.html", {"services": services})

def all_laptops(request):
    laptops = Laptop.objects.filter(is_available=True).order_by('-created_at')
    return render(request, 'all_laptops.html', {'laptops': laptops})

from .models import Laptop

def laptop_detail(request, id):
    laptop = Laptop.objects.get(id=id)
    all_laptops = Laptop.objects.exclude(id=id)[:6]  # exclude current laptop

    context = {
        'laptop': laptop,
        'all_laptops': all_laptops
    }
    return render(request, 'laptop_detail.html', context)

def review_page(request):

    if request.method == "POST":
        name = request.POST.get("name")
        rating = request.POST.get("rating")
        comment = request.POST.get("comment")

        if name and rating and comment:
            Review.objects.create(
                name=name,
                rating=int(rating),
                comment=comment
            )

        return redirect("review_page")

    reviews = Review.objects.filter(is_approved=True).order_by("-created_at")

    return render(request, "review.html", {"reviews": reviews})
def about(request):
    return render(request, "about.html")

def contact(request):
    return render(request, "contact.html")
def book_repair(request):
    return render(request, "book_repair.html")
def terms(request):
    return render(request, "terms.html")

def faq(request):
    return render(request, "faq.html")