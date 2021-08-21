from django.shortcuts import render, redirect
from django.contrib import messages

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
            # print("!!!!!!!!!!!!!!!")
            # print("CURRENT IMAGE:", img)
            # print("!!!!!!!!!!!!!!!")
            for element in str(img).split("'"):
                print("ELEMENT:", element)
                if "http" in element:
                    img = element

        try:
            price = soup.find("p", {"class":"wt-text-title-03 wt-mr-xs-2"}).text.strip()
        except:
            price = soup.find("div", {"class":"wt-order-xs-1 wt-mb-xs-0 wt-mb-sm-3"}).text.strip()
        price = price.split()[-1].replace("£", "").replace("+", "")

        # TODO: assign actual ID numbers when adding to database
        id_num = 243
        
        if product_name is not None:
            if img is not None:
                if price is not None:
                    messages.add_message(request, messages.SUCCESS, f"Product: [ {product_name} ] is successfully added!")
                    messages.add_message(request, messages.INFO, f'You can check the product with the ID Number: {id_num} in Product page.')
                else:
                    messages.add_message(request, messages.ERROR, "There was a problem with retrieving product price")
            else:
                messages.add_message(request, messages.ERROR, "There was a problem with retrieving image link of the product")
        else:
            messages.add_message(request, messages.ERROR, "There was a problem with retrieving product name")
        # print("-------")
        # print(product_name)
        # print("-------")
        # print(img)
        # print("-------")
        # print(price)

        return render(request, 'scraper/index.html')
    else:
        return render(request, 'scraper/index.html')

def product(request):
    return render(request, "scraper/product.html")

def products(request):
    return render(request, "scraper/products.html")
