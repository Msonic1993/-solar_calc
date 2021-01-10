from decimal import Decimal

from TypKlienta.models import klient


class PriceCalculationSystemmontazowy():


    MocInstalacji = klient.objects.last().MocInstalacji

    def __init__(self,modelform,CenaSystemuMontazowego):


        self.modelform = modelform
        self.CenaSystemuMontazowego = Decimal(CenaSystemuMontazowego)

        if modelform:
            self.WartoscSystemuMontazowego = ( self.MocInstalacji * Decimal(CenaSystemuMontazowego))

    def count_PriceCalculationSystemmontazowy(self):
        return self.WartoscSystemuMontazowego