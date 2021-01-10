from .models import klient,Moduly,Falowniki,Optymalizatory,Systemmontazowy
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm, Textarea
from django import forms



class DodajKlienta(ModelForm):

    class Meta:
        model = klient
        fields = ("typ","imie", "nazwisko", "ulica", "miasto", "telefon", "metraz","ekspozycjaDachowa", "kadNachyleniaDachu","zuzycie")
        labels = {
            'typ': 'Typ klienta',
            'imie': 'Imię klienta',
            'nazwisko': 'Nazwisko klienta',
            'ulica': 'Nazwa  i nr ulicy',
            'miasto': 'Nazwa miasta',
            'telefon': 'Telefon kontaktowy',
            'metraz': 'Metraż budynku',
            'ekspozycjaDachowa': 'Ekspozycja dachowa',
            'kadNachyleniaDachu': 'Kąd nachylenia dachu',
            'zuzycie': 'Zużycie roczne prądu',
            }

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



ELEMENTY_DODATKOWE_CHOICES = [
    ('NIE', 'NIE'),
    ('TAK', 'TAK'),

]
class ElementyDodatkoweForm(forms.Form):
    Zwyszka = forms.ChoiceField(choices=ELEMENTY_DODATKOWE_CHOICES,label="Zwyszka ")
    WiFiExtender = forms.ChoiceField(choices=ELEMENTY_DODATKOWE_CHOICES,label="WiFi Extender ")


PPOZ_CHOICES = [
    ('NIE', 'NIE'),
    ('TAK', 'TAK'),

]
class PPOZForm(forms.Form):

    KlientPPOZ = klient.objects.last().WymaganaMoc
    KlientPPOZFloat = float(str(KlientPPOZ))

    if KlientPPOZFloat > 6500:
         ObowiazkowePPOZ = forms.CharField(label='',
                    widget=forms.TextInput(attrs={'placeholder': 'Instalacja pow. 6,5 kW. Zabezpieczenie PPOŻ jest obowiązkowe', 'readonly':'readonly','size':55, 'maxlength':30},))
    else:
        ObowiazkowePPOZ = forms.ChoiceField(choices=PPOZ_CHOICES, label="Zabezpieczenie PPOŻ ")
