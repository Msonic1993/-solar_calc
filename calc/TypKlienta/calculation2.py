from decimal import Decimal


class PriceCalculation():



    def __init__(self,MocModulu,xx,modelform,Decimalform2,CenaModulu):

        self.MocModulu = Decimal(MocModulu)
        self.xx = Decimal(xx)
        self.modelform = modelform
        self.Decimalform2 = Decimal(Decimalform2)
        self.CenaModulu = CenaModulu


        if modelform:
            self.LiczbaModulow =(Decimal(xx)/ MocModulu/1000) + Decimal(Decimalform2)
            self.MocInstalacji = self.LiczbaModulow * self.MocModulu
            self.WartoscModulow =  self.LiczbaModulow * CenaModulu

    def count_PriceCalculation(self):
        return round(self.LiczbaModulow) , round(self.WartoscModulow,2), round( self.MocInstalacji,2)