from decimal import Decimal


class PriceCalculationFalowniki():



    def __init__(self,modelform,intform2,CenaFalownika1):


        self.modelform = modelform
        self.intform2 = int(intform2)
        self.CenaFalownika1 = Decimal(CenaFalownika1)


        if modelform:
            self.WartoscFalownikow =  self.intform2 * Decimal(CenaFalownika1)

    def count_PriceCalculationFalowniki(self):
        return self.WartoscFalownikow