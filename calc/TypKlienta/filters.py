import django_filters

from TypKlienta.models import klient


class KlientFilter(django_filters.FilterSet):

        class Meta:
            model = klient
            fields = fields = ['imie', 'nazwisko']