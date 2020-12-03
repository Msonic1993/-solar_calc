from TypKlienta.models import klient,KadNachyleniaDachu
from django.forms import ModelForm
from django import forms



class DodajKlienta(ModelForm):
    class Meta:
        model = klient
        fields = ("typ","imie", "nazwisko", "ulica", "miasto", "telefon", "metraz", "zuzycie")

class RoofSlopeAngleForm(forms.Form):
        # model = KadNachyleniaDachu
        # fields = ['kadnachylenia',]
        kadnachylenia = forms.ModelChoiceField(queryset=KadNachyleniaDachu.objects.all(),label="Wybierz kąt nachylenia dachu")

