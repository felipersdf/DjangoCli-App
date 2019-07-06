from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.http import HttpResponse
from .models import Client
from .forms import ClientForm, UserForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.

def home(request):
    return render(request, 'home.html')

def list_clients(request):
    clients = Client.objects.all()
    return render(request, 'clients.html', {'clients': clients})

def create_client(request):
    form = ClientForm(request.POST or None)
    
    if form.is_valid():
        form.save()
        return redirect('listar_clients')

    return render(request, 'new_client.html', {'form':form})

def edit_client(request, pk):
    client = Client.objects.get(pk=pk)
    form = ClientForm(request.POST or None, instance=client)

    if form.is_valid():
        form.save()
        return redirect('listar_clients')

    return render(request, 'updateclient.html', {'form': form, 'client': client})

def delete_client(request, pk):
    client = Client.objects.get(pk=pk)

    if request.method == 'POST':
        client.delete()
        return redirect('listar_clients')

    return render(request, 'deleteclient.html', {'cliente':client})

def user_login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user:
            if user.is_active:
                login(request,user)
                return redirect('home')
        else:
            return HttpResponse("O login falhou. Tente novamente.")
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        user_form = UserForm(data=request.POST)
        if user_form.is_valid():
            user = user_form.save()
            user.set_password(user.password)
            user.save()
            return redirect('home')
        else:
            print(user_form.errors)
    else:
        user_form = UserForm()
    return render(request,'registration.html',{'user_form':user_form})

def user_logout(request):
    logout(request)
    return redirect('home')