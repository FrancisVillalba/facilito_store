from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.conf import settings
from django.contrib import messages
from .models import BillingProfile
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.list import ListView

class BillingProfileListView(LoginRequiredMixin, ListView):
    login_url = 'vw-login'
    template_name = 'billing_profiles/billing_profiles.html'

    def get_queryset(self):
        return self.request.user.billing_profiles


# Create your views here.
@login_required(login_url='vw-login')
def create(request):
     
    if request.method == 'POST':
        if request.POST.get('stripeToken'):

            if not request.user.has_customer():
                request.user.create_customer_id()

            stripe_token = request.POST['stripeToken']
            billing_profile = BillingProfile.objects.create_by_stripe_token(request.user, stripe_token)

            if billing_profile:
                messages.success(request, 'Tarjeta creada exitosamente')

    return render(request, 'billing_profiles/create.html', {
        'stripe_public_key': settings.STRIPE_PUBLIC_KEY
    })