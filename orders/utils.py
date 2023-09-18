from django.urls import reverse
from .models import Order


def get_or_create_order(cart, request): 
    # order = Order.objects.filter(cart=cart).first()
    order = cart.order

    if order is None and request.user.is_authenticated:
        order = Order.objects.create(cart=cart, user=request.user)

    if order:
        request.session['order_id'] = order.order_id

    return order

def breadcrumb(products=True, address=False, payment=False, confirmation=False):
    return[
        {'title':'Productos', 'active': products, 'url': reverse('orders:order-view')},
        {'title':'Direccion', 'active': address, 'url': reverse('orders:address-view')},
        {'title':'Pago', 'active': payment, 'url': reverse('orders:order-view')},
        {'title':'Confirmación', 'active': confirmation, 'url': reverse('orders:order-view')},
    ]

def destroy_order(request):
    request.session['order_id'] = None