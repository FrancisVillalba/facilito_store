from django.shortcuts import render
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect
from django.contrib import messages

def login_vw(request):   
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
