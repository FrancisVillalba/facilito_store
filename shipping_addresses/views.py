from typing import Any
from django import http
from django.db.models.query import QuerySet
from django.http.response import HttpResponse
from django.shortcuts import get_object_or_404, render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView
from django.views.generic.edit import UpdateView, DeleteView
from .models import ShippingAddress
from .forms import ShippingAddressForm
from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin



class ShippingAddressListView(LoginRequiredMixin, ListView):
    login_url = 'vw-login'
    model = ShippingAddress
    template_name = 'shipping_addresses/shipping_addresses.html'

    def get_queryset(self):
        return ShippingAddress.objects.filter(user=self.request.user).order_by('-default')

class ShippingAddressUpdateView(LoginRequiredMixin, SuccessMessageMixin, UpdateView):
    login_url = 'vw-login'

    model = ShippingAddress
    form_class = ShippingAddressForm
    template_name = 'shipping_addresses/update.html'
    success_url = reverse_lazy('shipping_addresses:shipping-address-view')

    def get_success_url(self):
        return reverse('shipping_addresses:shipping-address-view')
    

    def dispatch(self, request, *args, **kwargs): 
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart-view')
        
        return super(ShippingAddressUpdateView, self).dispatch(request, *args, **kwargs)
    
class ShippingAddressDeleteView(LoginRequiredMixin, DeleteView):
    login_url = 'vw-login'
    model = ShippingAddress
    template_name = 'shipping_addresses/delete.html'
    success_url = reverse_lazy('shipping_addresses:shipping-address-view')

    def dispatch(self, request, *args, **kwargs):
        if self.get_object().defaul:
            return redirect('shipping_addresses:shipping-address-view')
        
        if request.user.id != self.get_object().user_id:
            return redirect('carts:cart-view')
        
        return super(ShippingAddressDeleteView, self).dispatch(request, *args, **kwargs)

@login_required(login_url='vw-login')
def create(request):
    form = ShippingAddressForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        shipping_address = form.save(commit=False)
        shipping_address.user = request.user
        shipping_address.default = not ShippingAddress.objects.filter(user=request.user).exists()

        shipping_address.save()

        messages.success(request,'Dirección creada con exito.')

        return redirect('shipping_addresses:shipping-address-view')

    return render(request, 'shipping_addresses/create.html',{
        'form': form
    })

def default(request, pk):
    shipping_address = get_object_or_404(ShippingAddress, pk=pk)

    if request.user.id != shipping_address.user_id:
        return redirect('carts:cart-view')
    
    if request.user.has_shipping_address():
        request.user.shipping_address.update_default()    
         
   
    shipping_address.update_default(True)

    return redirect('shipping_addresses:shipping-address-view')