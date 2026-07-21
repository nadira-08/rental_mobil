from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required

@login_required
def dashboard(request):
    return render(request, 'administrator/dashboard.html')

@login_required
def redirect_user(request):
    user = request.user

    if user.role == 'administrator':
        return redirect('/administrator/')
    elif user.role == 'petugas':
        return redirect('/petugas/')
    elif user.role == 'pelanggan':
        return redirect('/pelanggan/')

    return redirect('/admin/')