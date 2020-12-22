from decimal import Decimal

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

from .calculation10 import PriceZabezpieczeniePPOZ
from .calculation2 import PriceCalculation
from .calculation3 import PriceCalculationFalowniki
from .calculation4 import PriceCalculationOptymalizatory
from .calculation5 import PriceCalculationSystemmontazowy
from .calculation6 import PriceCalculationSkrzynkiAC
from .calculation7 import PriceCalculationLiczbaStringow
from .calculation8 import PriceCalculationPraceGruntowe
from .calculation9 import PriceCalculationElementyDodatkowe
from .forms import SignUpForm, OptymalizatoryForm, SystemMontazowyForm, SkrzynkiACForm, LiczbaStringowForm, \
    ElementyDodatkoweForm, PPOZForm
from .calculation import PowerComsumption
from .filters import KlientFilter
from .forms import DodajKlienta, ModulyForm, FalownikiForm
from .models import TypKlienta, Vat, klient, KadNachyleniaDachu, WymaganaMocInstalacji, EkspozycjaDachowa, Moduly, \
    Falowniki, Optymalizatory, Systemmontazowy
from .tables import KlientTable
from django_tables2.views import SingleTableMixin
from django.shortcuts import render


def index(request):
    if request.method == 'POST':
        form = DodajKlienta(request.POST)

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
            obliczenie = PowerComsumption(zuzycie, metraz, kadnachylenia, przelicznik, ekspozycja, mnoznik)
            wynik = obliczenie.count_Comsumption()

            GetId = klient.objects.get(imie=Imieklienta, nazwisko=NazwiskoKlienta, zuzycie=zuzycie,
                                       metraz=metraz).IdKlienta
            insertMocInstalacji = WymaganaMocInstalacji(IdKlienta=GetId, WymaganaMoc=wynik)
            insertMocInstalacji.save()

            x = WymaganaMocInstalacji.objects.get(IdKlienta=GetId).id
            klient.objects.filter(IdKlienta=GetId).update(WymaganaMoc_id=x)
            # klient.objects.filter(IdKlienta=GetId).update(field1='some value')

            return render(request, 'TypKlienta/glowna.html', {'wynik': wynik})
    return render(request, 'TypKlienta/glowna.html', {'form': DodajKlienta()})


def klienciListView(request):
    user_list = klient.objects.all()
    user_filter = KlientFilter(request.GET, queryset=user_list)
    return render(request, 'TypKlienta/klienci.html', {'filter': user_filter})


def KalkulacjaCenowa(request):
    y = klient.objects.last().WymaganaMoc

    if request.method == 'POST':
        form = ModulyForm(request.POST)
        form2 = request.POST['dodatkowaliczba']

        if form.is_valid():
            print("")
        else:
            modelform = form["Model"].value()
            Decimalform2 = str(form2)
            if Decimalform2 == "":
                Decimalform2 = 0.00

            MocModulu = Moduly.objects.get(model=modelform).moc
            CenaModulu = Moduly.objects.get(model=modelform).cenanetto
            SugerowanaMoc1 = klient.objects.last().WymaganaMoc
            xx = str(SugerowanaMoc1)
            obliczenie1 = PriceCalculation(MocModulu, xx, modelform, Decimalform2, CenaModulu)
            LiczbaModulow = obliczenie1.count_PriceCalculation()[0]
            WartoscModulow = obliczenie1.count_PriceCalculation()[1]
            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(KamId_id=request.user)
            klient.objects.filter(IdKlienta=LatestData).update(LiczbaModulow=LiczbaModulow)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscModulow=WartoscModulow)
            klient.objects.filter(IdKlienta=LatestData).update(NazwaModulu=modelform)

            return render(request, 'TypKlienta/kalkulacjacenowa.html',
                          {'SugerowanaMoc': y, 'LiczbaModulow': LiczbaModulow, 'WartoscModulow': WartoscModulow,
                           'modelform': modelform, 'form': ModulyForm(), 'form2': form2})
    return render(request, 'TypKlienta/kalkulacjacenowa.html', {'form': ModulyForm(), 'SugerowanaMoc': y})


def KalkulacjaFalownika(request):
    y = klient.objects.last().WymaganaMoc
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu

    if request.method == 'POST':
        form = FalownikiForm(request.POST)
        form2 = request.POST['IloscFalownikow']

        if form.is_valid():
            print("")
        else:
            modelform = form["Model"].value()
            intform2 = str(form2)
            if intform2 == "":
                intform2 = 0

            CenaFalownika = Falowniki.objects.get(model=modelform).cenanetto
            CenaFalownika1 = float(CenaFalownika)
            obliczenie1 = PriceCalculationFalowniki(modelform, intform2, CenaFalownika1)
            WartoscFalownikow = obliczenie1.count_PriceCalculationFalowniki()

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(LiczbaFalownikow=intform2)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscFalownikow=WartoscFalownikow)
            klient.objects.filter(IdKlienta=LatestData).update(NazwaFalownika=modelform)

            return render(request, 'TypKlienta/kalkulacjafalownika.html',
                          {'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr, 'NazwaModuluStr': NazwaModuluStr,
                           'WartoscFalownikow': WartoscFalownikow, 'modelform': modelform, 'form': FalownikiForm(),
                           'form2': form2})
    return render(request, 'TypKlienta/kalkulacjafalownika.html',
                  {'form': FalownikiForm(), 'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr,
                   'NazwaModuluStr': NazwaModuluStr})


def KalkulacjaOptymalizatory(request):
    y = klient.objects.last().WymaganaMoc
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika

    if request.method == 'POST':
        form = OptymalizatoryForm(request.POST)
        form2 = request.POST['IloscOptymalizatorow']

        if form.is_valid():
            print("")
        else:
            modelform = form["Model"].value()
            intform2 = str(form2)
            if intform2 == "":
                intform2 = 0

            CenaOptymalizatora = Optymalizatory.objects.get(model=modelform).cenanetto
            obliczenie1 = PriceCalculationOptymalizatory(modelform, intform2, CenaOptymalizatora)
            WartoscOptymalizatorow = obliczenie1.count_PriceCalculationOptymalizatory()

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(LiczbaOptymalizatorow=intform2)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscOptymalizatorow=WartoscOptymalizatorow)
            klient.objects.filter(IdKlienta=LatestData).update(NazwaOptymalizatora=modelform)

            return render(request, 'TypKlienta/kalkulacjaoptymaliztorymocy.html',
                          {'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr, 'NazwaModuluStr': NazwaModuluStr,
                           'WartoscOptymalizatorow': WartoscOptymalizatorow, 'LiczbaFalownikowStr': LiczbaFalownikowStr,
                           'NazwaFalownikaStr': NazwaFalownikaStr, 'modelform': modelform, 'form': OptymalizatoryForm(),
                           'form2': form2})
    return render(request, 'TypKlienta/kalkulacjaoptymaliztorymocy.html',
                  {'form': OptymalizatoryForm(), 'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr,
                   'NazwaModuluStr': NazwaModuluStr, 'LiczbaFalownikowStr': LiczbaFalownikowStr,
                   'NazwaFalownikaStr': NazwaFalownikaStr})


def KalkulacjaSystemMontazowy(request):
    y = klient.objects.last().WymaganaMoc
    yy = float(str(y))
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika
    LiczbaOptyalizatorowStr = klient.objects.last().LiczbaOptymalizatorow
    NazwaOptyalizatorowStr = klient.objects.last().NazwaOptymalizatora

    if request.method == 'POST':
        form = SystemMontazowyForm(request.POST)

        if form.is_valid():
            print("")
        else:
            modelform = form["Model"].value()

            CenaSystemuMontazowego = Systemmontazowy.objects.get(nazwa=modelform).cenanetto
            obliczenie1 = PriceCalculationSystemmontazowy(modelform, yy, CenaSystemuMontazowego)
            WartoscSystemuMontazowego = obliczenie1.count_PriceCalculationSystemmontazowy()

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(WartoscSystemuMontazowego=WartoscSystemuMontazowego)
            klient.objects.filter(IdKlienta=LatestData).update(NazwaSystemuMontazowego=modelform)

            return render(request, 'TypKlienta/kalkulacjasystemymontazowe.html',
                          {'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr, 'NazwaModuluStr': NazwaModuluStr,
                           'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                           'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                           'WartoscSystemuMontazowego': WartoscSystemuMontazowego,
                           'LiczbaFalownikowStr': LiczbaFalownikowStr, 'NazwaFalownikaStr': NazwaFalownikaStr,
                           'modelform': modelform, 'form': SystemMontazowyForm()})
    return render(request, 'TypKlienta/kalkulacjasystemymontazowe.html',
                  {'form': SystemMontazowyForm(), 'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr,
                   'NazwaModuluStr': NazwaModuluStr, 'LiczbaFalownikowStr': LiczbaFalownikowStr,
                   'NazwaFalownikaStr': NazwaFalownikaStr})


def KalkulacjaLiczbaStringow(request):
    y = klient.objects.last().WymaganaMoc
    yy = float(str(y))
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika
    LiczbaOptyalizatorowStr = klient.objects.last().LiczbaOptymalizatorow
    NazwaOptyalizatorowStr = klient.objects.last().NazwaOptymalizatora
    NazwaSystemuMontazowegoStr = klient.objects.last().NazwaSystemuMontazowego

    if request.method == 'POST':
        form = LiczbaStringowForm(request.POST)

        if form.is_valid():
            modelform = form.cleaned_data['LiczbaStringow']

            obliczenie1 = PriceCalculationLiczbaStringow(modelform)
            WartoscStringow = obliczenie1.count_PriceCalculationLiczbaStringow()
            WartoscStringow1 = str(WartoscStringow)

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(WartoscStringow=WartoscStringow)
            klient.objects.filter(IdKlienta=LatestData).update(IloscStringow=modelform)

            return render(request, 'TypKlienta/kalkulacjaliczbastringow.html', {'SugerowanaMoc': y,
                                                                                'LiczbaModulowStr': LiczbaModulowStr,
                                                                                'NazwaModuluStr': NazwaModuluStr,
                                                                                'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                                'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                                'LiczbaStringowForm': LiczbaStringowForm,
                                                                                'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                                'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                                'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr,
                                                                                'modelform': modelform,
                                                                                'form': LiczbaStringowForm(),
                                                                                'WartoscStringow1': WartoscStringow1})

    return render(request, 'TypKlienta/kalkulacjaliczbastringow.html', {'form': LiczbaStringowForm(),
                                                                        'SugerowanaMoc': y,
                                                                        'LiczbaModulowStr': LiczbaModulowStr,
                                                                        'NazwaModuluStr': NazwaModuluStr,
                                                                        'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                        'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                        'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                        'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                        'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr})


def KalkulacjaSkrzynkiAC(request):
    y = klient.objects.last().WymaganaMoc
    yy = float(str(y))
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika
    LiczbaOptyalizatorowStr = klient.objects.last().LiczbaOptymalizatorow
    NazwaOptyalizatorowStr = klient.objects.last().NazwaOptymalizatora

    if request.method == 'POST':
        form = SkrzynkiACForm(request.POST)

        if form.is_valid():
            modelform = form.cleaned_data['IloscSkrzynekAC']

            obliczenie1 = PriceCalculationSkrzynkiAC(modelform, yy)
            WartoscSkrzynekAC = obliczenie1.count_PriceCalculationSkrzynkiAC()[0]
            WartoscOkablowaniaAC = obliczenie1.count_PriceCalculationSkrzynkiAC()[1]
            WartoscOkablowaniaDC = obliczenie1.count_PriceCalculationSkrzynkiAC()[2]
            KosztTransportu = obliczenie1.count_PriceCalculationSkrzynkiAC()[3]
            KosztMontazu = obliczenie1.count_PriceCalculationSkrzynkiAC()[4]

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(WartoscSkrzynekAC=WartoscSkrzynekAC)
            klient.objects.filter(IdKlienta=LatestData).update(IloscSkrzynekAC=modelform)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscOkablowaniaAC=WartoscOkablowaniaAC)
            klient.objects.filter(IdKlienta=LatestData).update(WartoscOkablowaniaDC=WartoscOkablowaniaDC)
            klient.objects.filter(IdKlienta=LatestData).update(KosztTransportu=KosztTransportu)
            klient.objects.filter(IdKlienta=LatestData).update(KosztMontazu=KosztMontazu)

            return render(request, 'TypKlienta/kalkulacjaskrzynkiac.html',
                          {'SugerowanaMoc': y, 'KosztMontazu': KosztMontazu, 'LiczbaModulowStr': LiczbaModulowStr,
                           'NazwaModuluStr': NazwaModuluStr, 'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                           'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr, 'WartoscSkrzynekAC': WartoscSkrzynekAC,
                           'LiczbaFalownikowStr': LiczbaFalownikowStr, 'NazwaFalownikaStr': NazwaFalownikaStr,
                           'modelform': modelform, 'form': SkrzynkiACForm()})
    return render(request, 'TypKlienta/kalkulacjaskrzynkiac.html',
                  {'form': SkrzynkiACForm(), 'SugerowanaMoc': y, 'LiczbaModulowStr': LiczbaModulowStr,
                   'NazwaModuluStr': NazwaModuluStr, 'LiczbaFalownikowStr': LiczbaFalownikowStr,
                   'NazwaFalownikaStr': NazwaFalownikaStr})

def KalkulacjaPraceGruntowe(request):
    y = klient.objects.last().WymaganaMoc
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika
    LiczbaOptyalizatorowStr = klient.objects.last().LiczbaOptymalizatorow
    NazwaOptyalizatorowStr = klient.objects.last().NazwaOptymalizatora
    NazwaSystemuMontazowegoStr = klient.objects.last().NazwaSystemuMontazowego

    if request.method == 'POST':
        modelformIloscM2 = request.POST.get('modelformIloscM2')

        if modelformIloscM2:
            modelformIloscM2 = request.POST.get('modelformIloscM2')
            if modelformIloscM2 =="":
                modelformIloscM2 = 0.00
            obliczenie1 = PriceCalculationPraceGruntowe(modelformIloscM2)
            KosztPracGruntowych = obliczenie1.count_PriceCalculationPraceGruntowe()
            KosztPracGruntowych1 = str(KosztPracGruntowych)

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(KosztPracGruntowych=KosztPracGruntowych)
            klient.objects.filter(IdKlienta=LatestData).update(IloscPracGruntowych=modelformIloscM2)

            return render(request, 'TypKlienta/kalkulacjapracegruntowe.html', {'SugerowanaMoc': y,
                                                                                'LiczbaModulowStr': LiczbaModulowStr,
                                                                                'NazwaModuluStr': NazwaModuluStr,
                                                                                'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                                'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                                'LiczbaStringowForm': LiczbaStringowForm,
                                                                                'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                                'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                                'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr,

                                                                               'modelformIloscM2': modelformIloscM2,
                                                                                'KosztPracGruntowych1': KosztPracGruntowych1})

    return render(request, 'TypKlienta/kalkulacjapracegruntowe.html', {
                                                                        'SugerowanaMoc': y,
                                                                        'LiczbaModulowStr': LiczbaModulowStr,
                                                                        'NazwaModuluStr': NazwaModuluStr,
                                                                        'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                        'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                        'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                        'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                        'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr})


def KalkulacjaElementyDodatkowe(request):
    y = klient.objects.last().WymaganaMoc
    yy = float(str(y))
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika
    LiczbaOptyalizatorowStr = klient.objects.last().LiczbaOptymalizatorow
    NazwaOptyalizatorowStr = klient.objects.last().NazwaOptymalizatora
    NazwaSystemuMontazowegoStr = klient.objects.last().NazwaSystemuMontazowego

    if request.method == 'POST':
        form = ElementyDodatkoweForm(request.POST)

        if form.is_valid():
            modelform1 = form.cleaned_data['Zwyszka']
            modelform2 = form.cleaned_data['WiFiExtender']

            obliczenie1 = PriceCalculationElementyDodatkowe(modelform1,modelform2)
            KosztZwyszka = obliczenie1.count_PriceCalculationElementyDodatkowe()[0]
            KosztWiFiExtender = obliczenie1.count_PriceCalculationElementyDodatkowe()[1]


            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(Zwyszka=modelform1)
            klient.objects.filter(IdKlienta=LatestData).update(KosztZwyszka=KosztZwyszka)
            klient.objects.filter(IdKlienta=LatestData).update(WiFiExtender=modelform2)
            klient.objects.filter(IdKlienta=LatestData).update(KosztWiFiExtender=KosztWiFiExtender)


            return render(request, 'TypKlienta/kalkulacjaelementydodatkowe.html', {'SugerowanaMoc': y,
                                                                                'LiczbaModulowStr': LiczbaModulowStr,
                                                                                'NazwaModuluStr': NazwaModuluStr,
                                                                                'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                                'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                                'LiczbaStringowForm': LiczbaStringowForm,
                                                                                'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                                'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                                'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr,
                                                                                'modelform1': modelform1,
                                                                                'modelform2': modelform2,
                                                                                'form': ElementyDodatkoweForm(),
                                                                                    })

    return render(request, 'TypKlienta/kalkulacjaelementydodatkowe.html', {'form': ElementyDodatkoweForm(),
                                                                        'SugerowanaMoc': y,
                                                                        'LiczbaModulowStr': LiczbaModulowStr,
                                                                        'NazwaModuluStr': NazwaModuluStr,
                                                                        'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                        'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                        'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                        'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                        'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr})


def KalkulacjaPPOZ(request):
    y = klient.objects.last().WymaganaMoc
    yy = float(str(y))
    LiczbaModulowStr = klient.objects.last().LiczbaModulow
    NazwaModuluStr = klient.objects.last().NazwaModulu
    LiczbaFalownikowStr = klient.objects.last().LiczbaFalownikow
    NazwaFalownikaStr = klient.objects.last().NazwaFalownika
    LiczbaOptyalizatorowStr = klient.objects.last().LiczbaOptymalizatorow
    NazwaOptyalizatorowStr = klient.objects.last().NazwaOptymalizatora
    NazwaSystemuMontazowegoStr = klient.objects.last().NazwaSystemuMontazowego

    if request.method == 'POST':
        form = PPOZForm(request.POST)

        if form.is_valid():
          print("")
        else:
            modelform = form["ObowiazkowePPOZ"].value()
            print(modelform)
            print("modelform")
            obliczenie1 = PriceZabezpieczeniePPOZ(modelform, yy)
            KosztPPOZ = obliczenie1.count_PriceZabezpieczeniePPOZ()
            KosztPPOZ1 = Decimal(KosztPPOZ)

            LatestData = klient.objects.latest("data").IdKlienta
            klient.objects.filter(IdKlienta=LatestData).update(KosztPPOZ=KosztPPOZ1)


            return render(request, 'TypKlienta/kalkulacjappoz.html', {'SugerowanaMoc': y,
                                                                                'LiczbaModulowStr': LiczbaModulowStr,
                                                                                'NazwaModuluStr': NazwaModuluStr,
                                                                                'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                                'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                                'LiczbaStringowForm': LiczbaStringowForm,
                                                                                'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                                'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                                'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr,
                                                                                'modelform': modelform,
                                                                                'KosztPPOZ': KosztPPOZ,
                                                                                'form': PPOZForm(),
                                                                                    })

    return render(request, 'TypKlienta/kalkulacjappoz.html', {'form': PPOZForm(),
                                                                        'SugerowanaMoc': y,
                                                                        'LiczbaModulowStr': LiczbaModulowStr,
                                                                        'NazwaModuluStr': NazwaModuluStr,
                                                                        'LiczbaFalownikowStr': LiczbaFalownikowStr,
                                                                        'NazwaFalownikaStr': NazwaFalownikaStr,
                                                                        'LiczbaOptyalizatorowStr': LiczbaOptyalizatorowStr,
                                                                        'NazwaOptyalizatorowStr': NazwaOptyalizatorowStr,
                                                                        'NazwaSystemuMontazowegoStr': NazwaSystemuMontazowegoStr})




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
