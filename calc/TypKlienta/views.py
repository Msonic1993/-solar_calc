from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django_tables2 import SingleTableView
from django_filters.views import FilterView

from .calculation import PowerComsumption
from .filters import KlientFilter
from .forms import DodajKlienta, RoofSlopeAngleForm
from .models import TypKlienta, Vat, klient, KadNachyleniaDachu
from .tables import KlientTable
from django_tables2.views import SingleTableMixin
from django.shortcuts import render

def index(request):

    form2 = RoofSlopeAngleForm()
    if request.method == 'POST':
        form=DodajKlienta(request.POST)
        form2 = RoofSlopeAngleForm(request.POST)
        if form.is_valid() & form2.is_valid() :
            form.save()
            zuzycie = form.cleaned_data['zuzycie']
            metraz = form.cleaned_data['metraz']
            kadnachylenia = form2.cleaned_data['kadnachylenia']
            przelicznik = KadNachyleniaDachu.objects.get(kadnachylenia=kadnachylenia).przelicznik
            obliczenie =PowerComsumption(zuzycie,metraz,kadnachylenia,przelicznik)
            wynik = obliczenie.count_Comsumption()
            print(wynik)
            return render(request, 'TypKlienta/glowna.html', { 'wynik': wynik})
    return  render(request, 'TypKlienta/glowna.html', {'form': DodajKlienta(),'form2': RoofSlopeAngleForm() })

def  wynik(request):

    wynik1 = wynik

    return render(request,'TypKlienta/wynik.html', {'wynik1': wynik1},)

class  klienciListView(SingleTableMixin,FilterView):
    model = klient
    table_class = KlientTable
    template_name = 'TypKlienta/klienci.html'
    filter = KlientFilter()

