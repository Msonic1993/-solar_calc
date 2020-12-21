from decimal import Decimal


class PriceCalculationSystemmontazowy():

#1

    def __init__(self,modelform,yy,CenaSystemuMontazowego):


        self.modelform = modelform
        self.CenaSystemuMontazowego = Decimal(CenaSystemuMontazowego)
        self.yy =  Decimal(yy)

        if modelform:
            self.WartoscSystemuMontazowego = ( Decimal(yy) * Decimal(CenaSystemuMontazowego))/1000

    def count_PriceCalculationSystemmontazowy(self):
        return self.WartoscSystemuMontazowego