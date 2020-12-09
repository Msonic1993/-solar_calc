from TypKlienta.models import klient
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django import forms



class DodajKlienta(ModelForm):
    class Meta:
        model = klient
        fields = ("typ","imie", "nazwisko", "ulica", "miasto", "telefon", "metraz","ekspozycjaDachowa", "kadNachyleniaDachu","zuzycie")

# class RoofSlopeAngleForm(forms.Form):
#         # model = KadNachyleniaDachu
#         # fields = ['kadnachylenia',]
#         kadnachylenia = forms.ModelChoiceField(queryset=KadNachyleniaDachu.objects.all(),label="Wybierz kąt nachylenia dachu")
#
#
# class RoofExposition(forms.Form):
#     # model = KadNachyleniaDachu
#     # fields = ['kadnachylenia',]
#     ekspozycja = forms.ModelChoiceField(queryset=EkspozycjaDachowa.objects.all(),
#                                            label="Wybierz ekspozycje dachową")

class SignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    last_name = forms.CharField(max_length=30, required=False, help_text='Optional.')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username', 'email', 'password1', 'password2',)