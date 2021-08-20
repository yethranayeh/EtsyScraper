from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def index(request):
    return render(request, 'scraper/index.html')

def product(request):
    return render(request, "scraper/product.html")

def products(request):
    return render(request, "scraper/products.html")
