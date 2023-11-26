from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, get_user_model, login, logout
from .forms import EmployeeRegistrationForm, EmployeeLoginForm

# Create your views here.


def sign_up(request):
    next = request.GET.get('next')
    form = EmployeeRegistrationForm(request.POST or None)
    if form.is_valid():
        user = form.save(commit=False)
        password = form.cleaned_data.get('password')
        user.set_password(password)
        user.save()
        new_user = authenticate(username=user.username, password=password)
        login(request, new_user)
        if next:
            return redirect(next)
        return redirect('userapp:employee_login')
    
    data = {
        'form': form,
    }
    return render(request, 'userapp/Employee_SignUp.html', data)


def employee_login(request):
    next = request.GET.get('next')
    form = EmployeeLoginForm(request.POST or None)
    if form.is_valid():
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                request.session.set_expiry(420)
                login(request, user)
                return redirect('/')
            
    data = {
        'form':form
    }
    return render(request, 'userapp/Employee_login.html', data)


def logout_view(request):
    logout(request)
    return redirect('userapp:employee_login')

