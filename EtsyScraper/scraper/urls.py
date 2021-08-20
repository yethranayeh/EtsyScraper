from django.urls import path
from . import views

# If you want it to be at http://127.0.0.1:8000/
# first parameter of path should be ''
urlpatterns = [
    path('', views.index, name='index'),
    path('product', views.product, name='product'),
    path('products', views.products, name='products')
]
