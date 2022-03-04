from multiprocessing import context
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .form import ProductForm

def home(request):
    products = Product.objects.all()
    return render(request, 'app/dashboard.html', {'products': products})

def products(request):
    products = Product.objects.all()
    return render(request, 'app/products.html', {'products': products})

def createProduct(request):

    form = ProductForm ()
    if request.method == 'POST':
        form = ProductForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')

    context = {'form': form}
    return render(request, 'app/create_product.html', context)


def infoProduct(request, pk):

    form = ProductForm ()
    context = {'form': form}
    return render(request, 'app/create_product.html', context)


def deleteProduct(request, pk):

    product = Product.objects.get(id=pk)
    if request.method == "POST":
        product.delete()
        return redirect('/')

    context = {'item':product}
    return render(request,'app/delete.html', context)