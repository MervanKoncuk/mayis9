from django.shortcuts import render, redirect
from .forms import Kullanici
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
# Create your views here.
def kayit(request):
    form = Kullanici()
    if request.method == "POST":
        form = Kullanici(request.POST)
        if form.is_valid():
            user = form.save(commit= False)
            user.username = user.username.lower()
            user.save()
            messages.success(request, "Kaydınız oluşturuldu.")
            return redirect('login')
    context = {
        'form':form
    }
    return render(request, 'register.html', context)

def giris(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(request, username = username, password = password)

        if user is not None:
            login(request, user)
            messages.success(request, "Giriş yaptınız.")
            return redirect('index')
        else:
            messages.error(request, "Kullanıcı adı veya şifre hatalı.")
            return render(request, "login.html")

    return render(request, "login.html")

def userLogout(request):

    logout(request)
    messages.success(request, "Çıkış yapıldı")
    return redirect('index')