from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from .forms import PasswordForm
from .models import UserPassword
# Create your views here.

def passwords(request):

    return render(request, 'passwords/passwords.html',)

@login_required(login_url='user-login')
def edit_password(request, pk):
    app = UserPassword.objects.get(id=pk)
    password = UserPassword.objects.get(id=pk)
    form = PasswordForm(instance=app)
  
    if request.method == 'POST':
        app.app = request.POST['app']
        password.password = request.POST['password']
        app.save()
        password.save()
        return redirect('passwords', pk=pk)

    context = {'form': form}
    return render(request, 'topics/post_form.html', context)


@login_required(login_url='user-login')
def add_password(request, pk):
    form = PasswordForm()
    app = UserPassword.objects.get(id=pk)

    if request.method == 'POST':
        UserPassword.objects.create(
            user=request.user,
            app=request.POST['app'],
            password=request.POST.get('password')
        )
        return redirect('passwords', pk=pk)

    context = {"form":form}
    return render(request, 'passwords/passwords_add.html', context)

@login_required(login_url='user-login')
def delete_password(request, pk):
    app = UserPassword.objects.get(id=pk)
    password = UserPassword.objects.get(id=pk)
    
    if request.method == 'POST':
        app.delete()
        password.delete()
        return redirect('passwords')
    
    return render(request, 'passwords/delete.html')