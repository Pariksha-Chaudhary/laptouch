from django.contrib import admin
from .models import Service, Review , Laptop

# Register your models here.
@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name', 'starting_price', 'is_active']
    list_editable = ['is_active']

@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ['name', 'rating', 'is_approved']
    list_editable = ['is_approved']

@admin.register(Laptop)
class LaptopAdmin(admin.ModelAdmin):
    list_display = ('name', 'brand', 'condition', 'price', 'is_available')
    list_filter = ('condition', 'brand', 'is_available')
    search_fields = ('name', 'brand')