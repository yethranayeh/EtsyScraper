from django.shortcuts import render, redirect
from django.contrib import messages
from .models import Product

from bs4 import BeautifulSoup
import requests

# Create your views here.

def index(request):
    if request.method == "POST":
        link = request.POST["etsyLink"]

        page_content = requests.get(link).text

        soup = BeautifulSoup(page_content, "html.parser")

        try:
            product_name = soup.find("h1", {"class":"wt-text-body-03 wt-line-height-tight wt-break-word wt-mb-xs-1"}).text.strip()
        except:
            product_name = soup.find("p", {"class":"nla-listing-title wt-text-body-03 wt-line-height-tight wt-mb-xs-1 wt-mb-sm-2"}).text.strip()

        try:
            img = soup.find("li", {"class":"wt-position-absolute wt-width-full wt-height-full wt-position-top wt-position-left carousel-pane", "data-index":"0"}).find("img").get("src")
        except:
            img = soup.find("div", {"class":"nla-listing-image wt-width-full wt-height-full wt-rounded-01"})
            if img is not None:
                for element in str(img).split("'"):
                    if "http" in element:
                        img = element
            else:
                try:
                    img = soup.find("img", {"class":"wt-width-full wt-height-full wt-position-absolute wt-object-fit-cover"}).get("src")
                except:
                    img = None

        try:
            price = soup.find("p", {"class":"wt-text-title-03 wt-mr-xs-2"}).text.strip()
        except:
            price = soup.find("div", {"class":"wt-order-xs-1 wt-mb-xs-0 wt-mb-sm-3"}).text.strip()
        price = price.split()[-1].replace("£", "").replace("+", "")

        # TODO: assign actual ID numbers when adding to database
        
        if product_name is not None:
            if img is not None:
                if price is not None:
                    etsy_product = Product()
                    etsy_product.name = product_name
                    etsy_product.image = img
                    try:
                        etsy_product.price = float(price)
                        etsy_product.sold_out = False
                    except:
                        etsy_product.price = -1
                        etsy_product.sold_out = True
                    etsy_product.save()

                    # The print function below is to satisfy the back-end requirement for:
                    # > Adding Product Function: Gets the product link as an input, scraps the data from the website, saves the data to the database, and returns the Product Object (product_id, name, image, price) 
                    print("Adding Product Function:", etsy_product)

                    messages.add_message(request, messages.SUCCESS, f"Product: [ {product_name} ] is successfully added!")
                    messages.add_message(request, messages.INFO, f'You can check the product with the ID Number: {Product.objects.all().last().id} in Product page.')
                else:
                    messages.add_message(request, messages.ERROR, "There was a problem with retrieving product price")
            else:
                messages.add_message(request, messages.ERROR, "There was a problem with retrieving image link of the product")
        else:
            messages.add_message(request, messages.ERROR, "There was a problem with retrieving product name")

        return render(request, 'scraper/index.html')
    else:
        return render(request, 'scraper/index.html')

def product(request):
    if request.method == "POST":
        product_id = request.POST["product_id"]
        # print("requested id:", product_id)
        try:
            product = Product.objects.get(pk=product_id)

            # The print function below is to satisfy the back-end requirement for:
            # > Product Detail Function: Gets the product_id as input and returns the Product Object (product_id, name, image, price)
            print("Product Detail Function:", product)

            return render(
                request,
                "scraper/product.html",
                {"product":product}
            )
        except Exception as err:
            return render(
                request, 
                "scraper/product.html",
                {"wrong_id":product_id}
                )

    else:
        return render(request, "scraper/product.html")

def products(request):
    products = Product.objects.all()


    # The print function below is to satisfy the back-end requirement for:
    # > Product Detail Function: Gets the product_id as input and returns the Product Object (product_id, name, image, price)
    print("Product Detail Function:", products)


    return render(
        request, 
        "scraper/products.html", 
        {"products" : products}
        )
