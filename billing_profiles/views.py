from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required(login_url='vw-login')
def create(request):
    print("AAAAA")
    return render(request, 'billing_profiles/create.html', {

    })