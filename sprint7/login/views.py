from gettext import install
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth import login, authenticate, logout
from .forms import SignUpForm
from django.http import HttpResponse
from clientes.models import Cliente
from django.contrib import messages


# Create your views here.

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            
            dni = form.cleaned_data.get('dni')
            
            
            try: 
                newuser = Cliente.objects.get(customer_dni = dni)
                if newuser.user is None:

                    user = form.save()
                    newuser.user = user
                    newuser.save()
                else:
                    messages.error(request, 'El cliente ya tiene un usuario registrado')
                    return render(request, 'registration/signup.html', {'form': form})
                    # return HttpResponse('has account')
            except:
                    messages.error(request, 'No hay un cliente con ese DNI en nuestra base de datos')
                    return render(request, 'registration/signup.html', {'form': form})


            return redirect('login')
            
            
            
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})

def login2(request):
    return render(request, 'registration/login2.html')

def signout(request):
    logout(request)
    return redirect('login')