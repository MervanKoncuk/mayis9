from django import forms
from django.forms import ModelForm, widgets
from .models import Ogrenci


class OgrenciForm(ModelForm):
    class Meta:
        model = Ogrenci
        fields = ['isim_soyisim', 'hakkimda', 'resim']
    
    def __init__(self, *arg, **kwargs):
        super(OgrenciForm, self).__init__(*arg, **kwargs)



        self.fields['isim_soyisim'].widget.attrs.update({'class': 'form-control', 'placeholder': 'İsim ve Soyismi giriniz.'})
        self.fields['hakkimda'].widget.attrs.update({'class': 'form-control', 'placeholder': 'Kendinizi tanıtınız.'})
        self.fields['resim'].widget.attrs.update({'class': 'form-control'})