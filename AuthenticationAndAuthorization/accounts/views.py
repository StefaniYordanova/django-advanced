from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.forms import UserCreationForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import user_passes_test


def home_page(request: HttpRequest) -> HttpResponse:
    return render(request, 'accounts/home-page.html')


def fbv_login(request: HttpRequest) -> HttpResponse:
    username = request.POST.get('username')
    password = request.POST.get('password')

    user = authenticate(username=username, password=password)

    if user:
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/login.html')

def fbv_logout(request: HttpRequest) -> HttpResponse:
    if request.method == 'POST':
        logout(request)
        return redirect('home')


@user_passes_test(lambda user: not user.is_authenticated, login_url="home")
def register(request: HttpRequest) -> HttpResponse:
    form = UserCreationForm(request.POST or None)

    if form.is_valid():
        user = form.save()
        login(request, user)
        return redirect('home')

    return render(request, 'accounts/register.html', {'form': form})
