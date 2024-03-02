from django.shortcuts import render, redirect, resolve_url
from usuarios.forms import LoginForms, CadastroForms
from django.contrib.auth.models import User

def login(request):
    form = LoginForms()
    return render(request, "usuarios/login.html", {'form': form})

def cadastro(request):
    form = CadastroForms()
    
    if request.method == 'POST':
        form = CadastroForms(request.POST)
    
        if not form.is_valid():
            print(form.data, form.data['email'], form.errors)
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
