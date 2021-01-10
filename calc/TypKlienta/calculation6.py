from decimal import Decimal

from TypKlienta.models import klient


class PriceCalculationSkrzynkiAC():
    MocInstalacji = klient.objects.last().MocInstalacji
    def __init__(self,modelform,yy):
        self.yy=yy
        self.modelform = modelform

        if modelform:
            self.WartoscSkrzynekAC = modelform*600
            self.WartoscOkablowaniaAC = (self.MocInstalacji* 50)
            self.WartoscOkablowaniaDC =  (self.MocInstalacji * 90)
        if yy < 10000.00:
            self.KosztTransportu = 400
        else:
            if yy >= 10000.00 and yy <= 20000.00:
                self.KosztTransportu = 600
            else:
                if yy >= 20000.00 and yy <= 30000.00:
                    self.KosztTransportu = 800
                else:
                    self.KosztTransportu = 1000

        if yy < 8000.00:
            self.KosztMontazu = (yy*650.00)/1000.00
        else:
            if yy >= 8000.00 and yy <= 15000.00:
                self.KosztMontazu =  (yy*610.00)/1000.00
            else:
                self.KosztMontazu =  (yy*520.00)/1000.00

    def count_PriceCalculationSkrzynkiAC(self):
        return self.WartoscSkrzynekAC, self.WartoscOkablowaniaAC, self.WartoscOkablowaniaDC,self.KosztTransportu,self.KosztMontazu