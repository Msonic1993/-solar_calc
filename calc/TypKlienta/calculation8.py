from decimal import Decimal


class PriceCalculationPraceGruntowe():

    def __init__(self,modelformIloscM2):
        self.modelformIloscM2  =float(modelformIloscM2)

        if modelformIloscM2:
            self.KosztPracGruntowych = self.modelformIloscM2 * 30.00
        else:
            if modelformIloscM2 is None:
                self.KosztPracGruntowych = 0.00

    def count_PriceCalculationPraceGruntowe(self):
        return self.KosztPracGruntowych