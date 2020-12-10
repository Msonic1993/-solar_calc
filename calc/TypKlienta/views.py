from django.contrib.auth import authenticate, login
from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect, request
from django.urls import reverse
from django_tables2 import SingleTableView
from django_filters.views import FilterView
import datetime
from django.shortcuts import render, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse

from django.contrib.auth.forms import UserCreationForm
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from .calculation2 import PriceCalculation
from .forms import SignUpForm
from .calculation import PowerComsumption
from .filters import KlientFilter
from .forms import DodajKlienta,Moduly,Falowniki
from .models import TypKlienta, Vat, klient, KadNachyleniaDachu, WymaganaMocInstalacji, EkspozycjaDachowa
from .tables import KlientTable
from django_tables2.views import SingleTableMixin
from django.shortcuts import render

def index(request):


    if request.method == 'POST':
        form=DodajKlienta(request.POST)


        if form.is_valid():
            form.save()
            zuzycie = form.cleaned_data['zuzycie']
            metraz = form.cleaned_data['metraz']
            kadnachylenia = form.cleaned_data['kadNachyleniaDachu']
            ekspozycja = form.cleaned_data['ekspozycjaDachowa']
            Imieklienta = form.cleaned_data['imie']
            NazwiskoKlienta = form.cleaned_data['nazwisko']


            przelicznik = KadNachyleniaDachu.objects.get(kadnachylenia=kadnachylenia).przelicznik
            mnoznik = EkspozycjaDachowa.objects.get(ekspozycja=ekspozycja).mnoznik
            obliczenie =PowerComsumption(zuzycie,metraz,kadnachylenia,przelicznik,ekspozycja,mnoznik)
            wynik = obliczenie.count_Comsumption()

            GetId = klient.objects.get(imie=Imieklienta, nazwisko=NazwiskoKlienta,zuzycie=zuzycie,metraz=metraz).IdKlienta
            insertMocInstalacji = WymaganaMocInstalacji(IdKlienta= GetId, WymaganaMoc= wynik )
            insertMocInstalacji.save()

            x= WymaganaMocInstalacji.objects.get(IdKlienta=GetId).id
            klient.objects.filter(IdKlienta= GetId).update(WymaganaMoc_id=x)
            # klient.objects.filter(IdKlienta=GetId).update(field1='some value')

            return render(request, 'TypKlienta/glowna.html', { 'wynik': wynik})
    return  render(request, 'TypKlienta/glowna.html', {'form': DodajKlienta() })


def  klienciListView(request):
    user_list = klient.objects.all()
    user_filter = KlientFilter(request.GET, queryset=user_list)
    return render(request, 'TypKlienta/klienci.html', {'filter': user_filter})

def KalkulacjaCenowa(request):

    if request.method == 'POST':
        SugerowanaMoc = klient.objects.last().WymaganaMoc
        form=Moduly(request.POST)
        form1 = Falowniki(request.POST)

        model = ['model']
        # metraz = form.cleaned_data['metraz']
        # kadnachylenia = form.cleaned_data['kadNachyleniaDachu']
        # ekspozycja = form.cleaned_data['ekspozycjaDachowa']
        # Imieklienta = form.cleaned_data['imie']
        # NazwiskoKlienta = form.cleaned_data['nazwisko']
        MocModulu = 3
        SugerowanaMoc1 = 2
        obliczenie2 = PriceCalculation(MocModulu,SugerowanaMoc,model)
        LiczbaModulow = obliczenie2.count_PriceCalculation()

        return render(request, 'TypKlienta/kalkulacjacenowa.html', { 'SugerowanaMoc': SugerowanaMoc,'form': Moduly(),'form1': Falowniki(), 'LiczbaModulow': LiczbaModulow})





def register(request):

    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            for i in form:
                print(i)
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('index')

    else:
        form = SignUpForm()
    return render(request, 'TypKlienta/register.html', {'form': form})