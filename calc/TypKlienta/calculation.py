from .models import klient,KadNachyleniaDachu
from .forms import DodajKlienta
class PowerComsumption():



    def __init__(self,zuzycie,metraz,kadnachylenia,przelicznik,ekspozycja,mnoznik):

        self.zuzycie = zuzycie
        self.metraz = metraz
        self.kadnachylenia = kadnachylenia
        self.przelicznik = przelicznik
        self.ekspozycja = ekspozycja
        self.mnoznik = float(mnoznik)

        if kadnachylenia:

            self.wynik = zuzycie * przelicznik
        else:
            self.wynik = zuzycie

        if ekspozycja:
            self.wynik = float(self.wynik) *  float(mnoznik) * 1.2
        else:
            self.wynik = zuzycie

    def count_Comsumption(self):
        return self.wynik

