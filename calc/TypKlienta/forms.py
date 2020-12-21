from .models import klient,Moduly,Falowniki,Optymalizatory,Systemmontazowy
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

class ModulyForm(forms.Form):

     Model = forms.ModelChoiceField(
        queryset=Moduly.objects.values_list("model", flat=True).distinct(),
        empty_label=None
    )

class FalownikiForm(forms.Form):

    Model = forms.ModelChoiceField(
        queryset=Falowniki.objects.values_list("model", flat=True).distinct(),
        empty_label=None
    )

class OptymalizatoryForm(forms.Form):

    Model = forms.ModelChoiceField(
        queryset=Optymalizatory.objects.values_list("model", flat=True).distinct(),
        empty_label=""
    )


class SystemMontazowyForm(forms.Form):

    Model = forms.ModelChoiceField(
        queryset=Systemmontazowy.objects.values_list("nazwa", flat=True).distinct(),
        empty_label=""
    )

class SkrzynkiACForm(forms.Form):
    IloscSkrzynekAC = forms.IntegerField(label='Ilość skrzynek AC')


LICZBA_CHOICES = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
    ('6', '6'),
    ('7', '7'),
    ('8', '8'),
    ('9', '9'),
    ('10', '10'),
]

class LiczbaStringowForm(forms.Form):
    LiczbaStringow = forms.ChoiceField(choices=LICZBA_CHOICES,label="Liczba stringów ")

PRACE_GRUNTOWE_CHOICES = [
    ('NIE', 'NIE'),
    ('TAK', 'TAK'),

]
class PraceGrunoweForm(forms.Form):
    CzyPraceGruntowe = forms.ChoiceField(choices=PRACE_GRUNTOWE_CHOICES,label="Wybierz TAK lub NIE")

    if CzyPraceGruntowe =="TAK":
        IloscM2 = forms.IntegerField(label='Wpisz ilosc m2')

