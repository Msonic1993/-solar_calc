from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from django_tables2 import SingleTableView
from django_filters.views import FilterView
from .filters import KlientFilter
from .forms import DodajKlienta
from .models import TypKlienta, Vat,klient
from .tables import KlientTable
from django_tables2.views import SingleTableMixin
from django.shortcuts import render

def index(request):
    if request.method == 'POST':
        form=DodajKlienta(request.POST)
        if form.is_valid():
            form.save()
            # return HttpResponseRedirect(reverse('app_name:url_name'))

    return  render(request, 'TypKlienta/glowna.html', {
        'form': DodajKlienta(),
    })


class  klienciListView(SingleTableMixin,FilterView):
    model = klient
    table_class = KlientTable
    template_name = 'TypKlienta/klienci.html'
    filter = KlientFilter()

