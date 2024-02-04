from django.contrib.auth import views as auth_views
from django.contrib import messages
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import auth
from django.contrib.auth.views import PasswordResetView
from .forms import LoginForm  
def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password=request.POST['password'])
        
        if user is None:
            messages.error(request, 'Invalid email or password. Please try again.')
            return redirect('login')
        else:
            auth.login(request,user)
            return redirect('admin-panel')
    
    else:
        if request.user.is_authenticated:
            return redirect("admin-panel")
        form = LoginForm()

    return render(request, 'login.html', {'form': form})

@login_required(login_url='login')
def logout(request):
    auth.logout(request)
    return redirect("/login")




@login_required(login_url='login')
def admin_panel(request):
    return render(request, 'admin.html')


@login_required(login_url='login')
def create_user(request):
    return render(request, 'create_user.html')



