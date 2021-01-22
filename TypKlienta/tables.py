import django_tables2 as tables
from .models import klient

class KlientTable(tables.Table):
    class Meta:
        model = klient
        template_name = "django_tables2/bootstrap.html"
        fields = ("data","imie","nazwisko","ulica","miasto","telefon")

