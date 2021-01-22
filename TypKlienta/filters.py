import django_filters
from TypKlienta.models import klient


class KlientFilter(django_filters.FilterSet):


        class Meta:
            model = klient

            fields = ['imie', 'nazwisko','miasto']
        @property
        def qs(self):
            if self.request.user.is_authenticated:
                primary_queryset = super(KlientFilter, self).qs
                return primary_queryset.filter(KamId=self.request.user)
