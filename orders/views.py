from django.shortcuts import get_object_or_404, redirect, render
from carts.utils import get_or_create_cart
from shipping_addresses.models import ShippingAddress 
from .models import Order
from .utils import get_or_create_order, breadcrumb
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='vw-login')
def order(request): 
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    return render(request, 'orders/order.html', {
        'cart': cart, 
        'order': order,
        'breadcrumb': breadcrumb()
    })

@login_required(login_url='vw-login')
def address(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.shippingaddress_set.count() > 1

    return render(request, 'orders/address.html', {
        'cart' : cart,
        'order' : order,
        'breadcrumb': breadcrumb(address=True), 
        'sd': shipping_address,
        'can_choose_address': can_choose_address
    })

@login_required(login_url='vw-login')
def select_address(request):
    shipping_addresses = request.user.shippingaddress_set.all()

    return render(request, 'orders/select_address.html', {
        'breadcrumb': breadcrumb(address=True), 
        'shipping_addresses' : shipping_addresses
    })

@login_required(login_url='vw-login')
def check_address(request, pk):
     
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart-view')
    
    order.update_shipping_address(shipping_address)

    return redirect('orders:address-view')


@login_required(login_url='vw-login')
def confirm(request):
    cart = get_or_create_cart(request)
    order = get_or_create_order(cart, request)

    shipping_address = order.shipping_address
    if shipping_address is None:
        return redirect('orders:address-view')
    
    return render(request, 'orders/confirm.html',{
        'cart': cart,
        'order': order,
        'shipping_address' : shipping_address,
        'breadcrumb': breadcrumb(address=True, confirmation=True), 
    })

