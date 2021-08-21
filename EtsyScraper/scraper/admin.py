from django.contrib import admin
from .models import Product

class ProductAdmin(admin.ModelAdmin):
    # Displays id, name, created_date as columns in panel
    list_display = ("id", "name", "price", "sold_out")
    # makes "id" and "name" entries clickable
    list_display_links = ("id", "name")
    # creates filter by column feature
    list_filter = ("name", "price",)

    # adds a search field
    # it can search within the columns specified
    search_fields = ("name", "price")
    # the amount of elements that will be shown per page
    list_per_page = 20

# Register your models here.

admin.site.register(Product, ProductAdmin)
