from TypKlienta.models import klient
from django.forms import ModelForm


class DodajKlienta(ModelForm):
    class Meta:
        model = klient
        fields = ("typ","imie", "nazwisko", "ulica", "miasto", "telefon", "metraz", "")