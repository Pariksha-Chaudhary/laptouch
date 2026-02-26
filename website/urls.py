from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('services/', views.all_services, name='all_services'),
    path('laptops/', views.all_laptops, name='all_laptops'),
    path('laptop/<int:id>/', views.laptop_detail, name='laptop_detail'),
    path("reviews/", views.review_page, name="review_page"),
    path("about/", views.about, name="about"),
    path("contact/", views.contact, name="contact"),
    path("book-repair/", views.book_repair, name="book_repair"),
    path("terms/", views.terms, name="terms"),
    path("faq/", views.faq, name="faq"),

]