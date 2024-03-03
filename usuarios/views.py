from django.shortcuts import render, redirect, resolve_url
from usuarios.forms import LoginForms, CadastroForms
from django.contrib import auth, messages
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
    
    if request.method == 'POST':
        form = LoginForms(request.POST)
        
        if form.is_valid():
            usuario = auth.authenticate(
                    request=request, 
                    username=form.data.get('username'), 
                    password=form.data.get('password')
                )
            if usuario:
                auth.login(request, usuario)
                messages.add_message(request, messages.SUCCESS, message="Usuário logado com sucesso!")
                return redirect(resolve_url('usuarios.login'))
            else:
                messages.add_message(request, messages.ERROR, message="Usuário ou senha incorretos")
        else:
            messages.add_message(request, messages.ERROR, message="Erro ao efetuar login")

    return render(request, "usuarios/login.html", {'form': form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
    
        if not form.is_valid():
            return redirect(resolve_url('usuarios.cadastro'), {'form': form})
        else:
            user = User.objects.filter(username=form.data.get('username'))
            if not user.exists():
                usuario = User.objects.create_user(
                        username=form.data.get('username'),
                        email=form.data.get('email'),
                        password=form.data.get('password'),
                        is_staff=True
                    )
                usuario.save()
                return redirect(resolve_url('usuarios.login'))
            else:
                return redirect(resolve_url('usuarios.cadastro'), {'form': form})
    
    return render(request, "usuarios/cadastro.html", {'form': form})

def logout(request):
    auth.logout(request)
    messages.add_message(request, messages.SUCCESS, message="Logout efetuado com sucesso")
    return redirect('galeria.index')