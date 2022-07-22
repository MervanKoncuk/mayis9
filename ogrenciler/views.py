from django.shortcuts import render, redirect
from .models import Ogrenci
from .forms import OgrenciForm
from django.contrib import messages
from django.contrib.auth.models import User
# Create your views here.
def index(request):
    # ogrenciler = Ogrenci.objects.all()
    kullanicilar = User.objects.all()
    """ if request.user.is_authenticated:
        ogrenciler = Ogrenci.objects.filter(olusturan = request.user)
    else: """
    deneme = Ogrenci.objects.filter(olusturan = 1)
    print(deneme)
    ogrenciler = Ogrenci.objects.all()
    context = {
        'ogrenci':ogrenciler,
        'kullanicilar':kullanicilar
    }
    
    return render(request, "index.html", context)

def details(request, id):
    ogrenci = Ogrenci.objects.filter(id = id)
    context = {
        'ogrenci':ogrenci
    }
    return render(request, "details.html", context)

def create(request):
    form = OgrenciForm()
    context = {
        'form':form
    }
    # print(request.path)
    if request.method == 'POST':
        form = OgrenciForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('index')
        else:
            return render(request, "create.html", context)
    return render(request, "create.html", context) 

def filtrele(request, name):
    ogrenciler = Ogrenci.objects.filter(olusturan = name) 
    kullanicilar = User.objects.all()
    context = {
        'ogrenci':ogrenciler,
        'kullanicilar':kullanicilar
    }
    return render(request, "filtre.html", context)