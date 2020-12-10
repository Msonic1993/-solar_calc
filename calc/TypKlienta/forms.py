from TypKlienta.models import klient,Moduly,Falowniki
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class DodajKlienta(ModelForm):
    class Meta:
        model = klient
        fields = ("typ","imie", "nazwisko", "ulica", "miasto", "telefon", "metraz","ekspozycjaDachowa", "kadNachyleniaDachu","zuzycie")


class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)

class Moduly(forms.Form):

    Producent = forms.ModelChoiceField(
            queryset=Moduly.objects.values_list("producent", flat=True).distinct(),
            empty_label=None
        )
    Model = forms.ModelChoiceField(
        queryset=Moduly.objects.values_list("model", flat=True).distinct(),
        empty_label=None
    )

class Falowniki(forms.Form):

    Producent = forms.ModelChoiceField(
            queryset=Falowniki.objects.values_list("producent", flat=True).distinct(),
            empty_label=None
        )
    Model = forms.ModelChoiceField(
        queryset=Falowniki.objects.values_list("model", flat=True).distinct(),
        empty_label=None
    )
