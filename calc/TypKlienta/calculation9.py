from decimal import Decimal


class PriceCalculationElementyDodatkowe():

    def __init__(self,modelform1,modelform2):
        self.modelform1  = modelform1
        self.modelform2 = modelform2

        if modelform1  == "TAK":
            self.KosztZwyszka=800.00
        else:
            self.KosztZwyszka = 0.00

        if modelform2 == "TAK":
            self.KosztWiFiExtender=100.00
        else:
            self.KosztWiFiExtender = 0.00

    def count_PriceCalculationElementyDodatkowe(self):
        return self.KosztZwyszka, self.KosztWiFiExtender