from decimal import Decimal


class PriceCalculationFalowniki():



    def __init__(self,modelform,intform2,CenaFalownika):


        self.modelform = modelform
        self.intform2 = int(intform2)
        self.CenaFalownika = Decimal(CenaFalownika)


        if modelform:
            self.WartoscFalownikow =  self.intform2 * CenaFalownika

    def count_PriceCalculationFalowniki(self):
        return self.WartoscFalownikow