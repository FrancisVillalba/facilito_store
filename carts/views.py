from django.shortcuts import render
from .models import Cart
from .utils import get_or_create_cart
from products.models import Product

# Create your views here.
def cart(request):
    
    cart = get_or_create_cart(request)

    return render(request, 'carts/cart.html',{

    })

def add(request):
    print("xdddddddd")
    print(request)
    cart = get_or_create_cart(request)
    product = Product.objects.get(pk=request.POST.get('product_id'))

    cart.products.add(product)
    print(product)
    return render(request, 'carts/add.html', {
        'product' : product
    })