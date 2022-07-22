from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Ogrenci(models.Model):
    isim_soyisim = models.CharField(max_length=100, verbose_name="İsim-Soyisim")
    hakkimda = models.TextField(max_length=300, verbose_name="Hakkımda")
    resim = models.FileField(upload_to="ogrenciResmi/", null=True, blank=True, verbose_name="Öğrenci Resmi")
    olusturan = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    def __str__(self):
        return self.isim_soyisim