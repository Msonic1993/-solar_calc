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
from .calculation3 import PriceCalculationFalowniki
from .calculation4 import PriceCalculationOptymalizatory
from .forms import SignUpForm, OptymalizatoryForm
from .calculation import PowerComsumption
from .filters import KlientFilter
from .forms import DodajKlienta,ModulyForm,FalownikiForm
from .models import TypKlienta, Vat, klient, KadNachyleniaDachu, WymaganaMocInstalacji, EkspozycjaDachowa, Moduly,Falowniki,Optymalizatory
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
    y= klient.objects.last().WymaganaMoc

    if request.method == 'POST':
        form=ModulyForm(request.POST)
        form2 = request.POST['dodatkowaliczba']

        if form.is_valid():
           print("")
        else:
            modelform= form["Model"].value()
            Decimalform2= str(form2)
            if Decimalform2 =="":
                Decimalform2 = 0.00

            MocModulu = Moduly.objects.get(model=modelform).moc
            CenaModulu = Moduly.objects.get(model=modelform).cenanetto
            SugerowanaMoc1 = klient.objects.last().WymaganaMoc
            xx = str(SugerowanaMoc1)
            obliczenie1 = PriceCalculation(MocModulu, xx,modelform,Decimalform2,CenaModulu)
            LiczbaModulow = obliczenie1.count_PriceCalculation()[0]
            WartoscModulow= obliczenie1.count_PriceCalculation()[1]
            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(LiczbaModulow=LiczbaModulow)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscModulow=WartoscModulow)
            klient.objects.filter(IdKlienta=LatestData).update(NazwaModulu=modelform)

            return render(request, 'TypKlienta/kalkulacjacenowa.html',{'SugerowanaMoc': y,'LiczbaModulow': LiczbaModulow,'WartoscModulow': WartoscModulow, 'modelform': modelform,'form': ModulyForm(),'form2':form2 })
    return  render(request, 'TypKlienta/kalkulacjacenowa.html' ,{'form': ModulyForm(),'SugerowanaMoc': y })


def KalkulacjaFalownika(request):
    y= klient.objects.last().WymaganaMoc
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu

    if request.method == 'POST':
        form=FalownikiForm(request.POST)
        form2 = request.POST['IloscFalownikow']

        if form.is_valid():
           print("")
        else:
            modelform= form["Model"].value()
            intform2= str(form2)
            if intform2 =="":
                intform2 = 0

            CenaFalownika = Falowniki.objects.get(model=modelform).cenanetto
            obliczenie1 = PriceCalculationFalowniki(modelform,intform2,CenaFalownika)
            WartoscFalownikow = obliczenie1.count_PriceCalculationFalowniki()

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(LiczbaFalownikow=intform2)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscFalownikow=WartoscFalownikow)
            klient.objects.filter(IdKlienta=LatestData).update(NazwaFalownika=modelform)

            return render(request, 'TypKlienta/kalkulacjafalownika.html',{'SugerowanaMoc': y,'LiczbaModulowStr': LiczbaModulowStr,'NazwaModuluStr': NazwaModuluStr,'WartoscFalownikow': WartoscFalownikow, 'modelform': modelform,'form': FalownikiForm(),'form2':form2 })
    return  render(request, 'TypKlienta/kalkulacjafalownika.html' ,{'form': FalownikiForm(),'SugerowanaMoc': y,'LiczbaModulowStr': LiczbaModulowStr,'NazwaModuluStr': NazwaModuluStr })


def KalkulacjaOptymalizatory(request):
    y= klient.objects.last().WymaganaMoc
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika

    if request.method == 'POST':
        form=OptymalizatoryForm(request.POST)
        form2 = request.POST['IloscOptymalizatorow']

        if form.is_valid():
           print("")
        else:
            modelform= form["Model"].value()
            intform2= str(form2)
            if intform2 =="":
                intform2 = 0

            CenaOptymalizatora = Optymalizatory.objects.get(model=modelform).cenanetto
            obliczenie1 = PriceCalculationOptymalizatory(modelform,intform2,CenaOptymalizatora)
            WartoscOptymalizatorow = obliczenie1.count_PriceCalculationOptymalizatory()

            # LatestData = klient.objects.latest("data").IdKlienta
            # klient.objects.filter(IdKlienta=LatestData).update(LiczbaFalownikow=intform2)
            # klient.objects.filter(IdKlienta=LatestData).update(WartoscFalownikow=WartoscFalownikow)
            # klient.objects.filter(IdKlienta=LatestData).update(NazwaFalownika=modelform)

            return render(request, 'TypKlienta/kalkulacjaoptymaliztorymocy.html',{'SugerowanaMoc': y,'LiczbaModulowStr': LiczbaModulowStr,'NazwaModuluStr': NazwaModuluStr,'WartoscOptymalizatorow': WartoscOptymalizatorow,'LiczbaFalownikowStr': LiczbaFalownikowStr,'NazwaFalownikaStr': NazwaFalownikaStr ,'modelform': modelform,'form': OptymalizatoryForm(),'form2':form2 })
    return  render(request, 'TypKlienta/kalkulacjaoptymaliztorymocy.html' ,{'form': OptymalizatoryForm(),'SugerowanaMoc': y,'LiczbaModulowStr': LiczbaModulowStr,'NazwaModuluStr': NazwaModuluStr,'LiczbaFalownikowStr': LiczbaFalownikowStr,'NazwaFalownikaStr': NazwaFalownikaStr })



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