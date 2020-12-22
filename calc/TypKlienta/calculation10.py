from decimal import Decimal


class PriceZabezpieczeniePPOZ():

    def __init__(self,modelform,yy):
        self.modelform  =str(modelform)
        self.yy = yy

        if self.modelform == "TAK" or self.modelform == "" :
            if Decimal(yy) < 15000.00:
                self.KosztPPOZ = 1500.00
            else:
                if Decimal(yy) >= 15000.00 and Decimal(yy) <= 25000.00:
                    self.KosztPPOZ = 2500.00
                else:
                    if Decimal(yy) > 25000.00:
                        self.KosztPPOZ = 3500.00
        else:
            self.KosztPPOZ = 0.00


    def count_PriceZabezpieczeniePPOZ(self):
        return self.KosztPPOZ