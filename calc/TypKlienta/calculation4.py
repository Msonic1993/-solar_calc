from decimal import Decimal


class PriceCalculationOptymalizatory():



    def __init__(self,modelform,intform2,CenaOptymalizatora):


        self.modelform = modelform
        self.intform2 = int(intform2)
        self.CenaOptymalizatora = Decimal(CenaOptymalizatora)


        if modelform:
            self.WartoscOptymalizatoroww =  self.intform2 * CenaOptymalizatora

    def count_PriceCalculationOptymalizatory(self):
        return self.WartoscOptymalizatoroww