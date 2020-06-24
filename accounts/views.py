from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib import auth


def signup(request):
    if request.method == 'POST':
        if request.POST['pass'] == request.POST['confirmpass']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/signup.html', {'error': 'Usuário já cadastrado'})
            except User.DoesNotExist:
                user = User.objects.create_user(
                    username=request.POST['username'], password=request.POST['pass'])
                return redirect('login')
        else:
            return render(request, 'accounts/signup.html', {'pass_error': 'Senhas não combinam'})
    else:
        return render(request, 'accounts/signup.html')


def login(request):
    if request.method == 'POST':
        user = auth.authenticate(
            username=request.POST['username'], password=request.POST['pass'])
        if user is not None:
            auth.login(request, user)
            return redirect('lista_empregados')
        else:
            messages.error(request, 'Usuário ou Senha inválidos')
            return render(request, 'accounts/login.html')
    else:
        return render(request, 'accounts/login.html')


def logout(request):
    if request.method == 'POST':
      auth.logout(request)
      return redirect('login')
