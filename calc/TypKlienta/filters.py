import django_filters
from django.forms import forms
from django_filters import DateFilter

from TypKlienta.models import klient


class KlientFilter(django_filters.FilterSet):
    class Meta:
        model = klient
        fields = ['imie']