from urllib import request
from .models import Cart


def get_or_create_cart(request):

    # request.session['cart_id'] = None
    user = request.user if request.user.is_authenticated else None
    cart_id = request.session.get('cart_id')
    # Obtendremos el valor de una session
    # valor = request.session.get('card_id')
    # print(valor)

    # # Eliminar una session
    # request.session['card_id'] = None

    # Si no encuentra nada retorna None
    cart = Cart.objects.filter(cart_id=cart_id).first()

    if cart is None:
        cart = Cart.objects.create(user=user)

    if user and cart.user is None:
        cart.user = user
        cart.save()
    
    request.session['cart_id'] = cart.cart_id

    return cart