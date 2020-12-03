from .models import klient,KadNachyleniaDachu
from .forms import RoofSlopeAngleForm
class PowerComsumption():
    RoofSlopeAngleForm()


    def __init__(self,zuzycie,metraz,kadnachylenia,przelicznik):

        self.zuzycie = zuzycie
        self.metraz = metraz
        self.kadnachylenia = kadnachylenia
        self.przelicznik = przelicznik

        if kadnachylenia:

            self.wynik = zuzycie * przelicznik
        else:
            self.wynik = zuzycie

    def count_Comsumption(self):
        return self.wynik