from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages
from .forms import RegisterForm
from django.contrib.auth.models import User

 

def login_vw(request):  
    if request.user.is_authenticated:
        return redirect('vw-index')


    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(username=username, password=password)
        if user:
            login(request, user)
            messages.success(request, 'Bienvenido {}'.format(user.username))
            return redirect('vw-index')
        else:
            messages.error(request, 'Usuario o contraseña no validos')
        
              
    return render( request,"users/login.html", {

    })

def register_vw(request):  
    print('HOLAAAAAAAA1')  
    if request.user.is_authenticated:
        print('HOLAAAAAAAA')
        return redirect('vw-index')
    
    print('HOLAAAAAAAA2')
    form = RegisterForm(request.POST or None)

    if request.method == 'POST' and form.is_valid():
        # username =  form.cleaned_data.get('username')
        # email =  form.cleaned_data.get('email')
        # password =  form.cleaned_data.get('password')

        # user = User.objects.create_user(username, email, password)
        user = form.save()
        if user:
            login(request, user)
            messages.success(request, 'Creado exitosamente')

            return redirect('vw-index')

    return render(request, 'users/register.html',{
         'form' : form
     })

def logout_vw(request):   
    logout(request)

    messages.success(request, 'Sessión cerrada')
    return redirect('vw-login')

def index(request): 
    
    return render(
        request,
        "index.html",
        {
            "message": "Listado de productos",
            "title": "Productos",
            "products": [
                {"title": "Playera", "price": 5, "stock": True},
                {"title": "Camisa", "price": 7, "stock": True},
                {"title": "Mochila", "price": 20, "stock": False}
            ],
        }
    )
