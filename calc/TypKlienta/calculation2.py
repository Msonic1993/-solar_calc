from decimal import Decimal


class PriceCalculation():



    def __init__(self,MocModulu,xx,modelform,Decimalform2):

        self.MocModulu = Decimal(MocModulu)
        self.xx = Decimal(xx)
        self.modelform = modelform
        self.Decimalform2 = Decimal(Decimalform2)


        if modelform:
            self.LiczbaModulow =(Decimal(xx)/ MocModulu/1000) + Decimal(Decimalform2)


    def count_PriceCalculation(self):
        return self.LiczbaModulow