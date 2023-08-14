from typing import Any, Dict
from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.detail import DetailView
from products.models import Product
# Create your views here.

class ProductListView(ListView):
    template_name = 'index.html'
    queryset = Product.objects.all().order_by('-id')

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs) 
        context['message'] = 'Listado de productos'


        return context
    
class ProductDetailView(DetailView):
    model = Product
    template_name = 'products/product.html'

    def get_context_data(self, **kwargs: Any):
        context =  super().get_context_data(**kwargs)  

        return context