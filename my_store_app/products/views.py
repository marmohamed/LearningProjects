from re import template
from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .models import Product

# Create your views here.
def products(request):
    allProducts = Product.objects.all().values()
    template = loader.get_template('products/all_products.html')
    context = {
        'allProducts': allProducts
    }
    return HttpResponse(template.render(context, request))


def details(request, id):
    myproduct = Product.objects.get(id=id)
    template = loader.get_template('products/details.html')
    context = {
        'myproduct': myproduct
    }
    return HttpResponse(template.render(context, request))