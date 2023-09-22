from django.shortcuts import get_object_or_404, redirect, render
from carts.utils import get_or_create_cart, destroy_cart
from charges.models import Charge
from .mails import Mail
from shipping_addresses.models import ShippingAddress 
from .models import Order
from .utils import get_or_create_order, breadcrumb, destroy_order
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView
from django.db.models.query import EmptyQuerySet
from .decorators import validate_cart_and_order
from django.db import transaction

class OrderListView(LoginRequiredMixin, ListView):
    login_url = 'vw-login'
    template_name = 'orders/orders.html'

    def get_queryset(self):
        return self.request.user.orders_completed()

# Create your views here.
@login_required(login_url='vw-login')
@validate_cart_and_order
def order(request, cart, order): 
    # cart = get_or_create_cart(request)
    # order = get_or_create_order(cart, request)

    if not cart.has_products():
        return redirect('carts:cart-view')

 
    return render(request, 'orders/order.html', {
        'cart': cart, 
        'order': order,
        'breadcrumb': breadcrumb()
    })

@login_required(login_url='vw-login')
@validate_cart_and_order
def address(request, cart, order):
    # cart = get_or_create_cart(request)
    # order = get_or_create_order(cart, request)
    if not cart.has_products():
        return redirect('carts:cart-view')
    
    shipping_address = order.get_or_set_shipping_address()
    can_choose_address = request.user.has_shipping_addresses() 

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
@validate_cart_and_order
def check_address(request, cart, order, pk): 
    # cart = get_or_create_cart(request)
    # order = get_or_create_order(cart, request)

    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart-view')
    
    order.update_shipping_address(shipping_address)

    return redirect('orders:address-view')

@login_required(login_url='vw-login')
@validate_cart_and_order
def payment(request, cart, order):

    if not cart.has_products() or order.shipping_address is None:
        return redirect('carts:cart-view')
    

    billing_profile = order.get_or_set_billing_profile()

    return render(request,'orders/payment.html',{
        'cart': cart,
        'order': order,
        'billing_profile' : billing_profile,
        'breadcrumb': breadcrumb(address=True, payment=True, confirmation=True)
    })

@login_required(login_url='vw-login')
@validate_cart_and_order
def confirm(request, cart, order):

    if not cart.has_products() or order.shipping_address is None or order.billing_profile is None:
        return redirect('carts:cart-view')
    

    # cart = get_or_create_cart(request)
    # order = get_or_create_order(cart, request)

    shipping_address = order.shipping_address
    if shipping_address is None:
        return redirect('orders:address-view')
    
    return render(request, 'orders/confirm.html',{
        'cart': cart,
        'order': order,
        'shipping_address' : shipping_address,
        'breadcrumb': breadcrumb(address=True, confirmation=True), 
    })

@login_required(login_url='vw-login')
def cancel(request):
     
    #  Se puedo obtimizar usando el decorador @validate_cart_and_order
     cart = get_or_create_cart(request)
     order = get_or_create_order(cart, request)

     if request.user.id != order.user_id:
         return redirect('carts:cart-view')
     
     order.cancel()

     destroy_order(request)
     destroy_cart(request)

     messages.error(request, 'Orden cancelada')
     return redirect('vw-index')

@login_required(login_url='vw-login')
def complete(request):
     #  Se puedo obtimizar usando el decorador @validate_cart_and_order
     cart = get_or_create_cart(request)
     order = get_or_create_order(cart, request)

     if request.user.id != order.user_id:
         return redirect('carts:cart-view')
     
     charge = Charge.objects.create_charge(order)
     if charge: 
        with transaction.atomic(): 
            order.complete()

            # thread = threading.Thread(target=Mail.send_complete_order, args=(
            #     order, request.user
            # ))
            # thread.start()

        #  Mail.send_complete_order(order, request.user)

            destroy_order(request)
            destroy_cart(request)

            messages.success(request, 'Compra completada exitosamente')

     return redirect('vw-index')

