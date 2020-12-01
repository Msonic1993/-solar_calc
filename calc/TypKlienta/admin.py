from django.contrib import admin
from .models import TypKlienta, Vat, KadNachyleniaDachu, EkspozycjaDachowa, klient

# Register your models here.

admin.site.register(klient)
admin.site.register(TypKlienta)
admin.site.register(Vat)
admin.site.register(KadNachyleniaDachu)
admin.site.register(EkspozycjaDachowa)
