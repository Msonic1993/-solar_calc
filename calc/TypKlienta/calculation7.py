from decimal import Decimal


class PriceCalculationLiczbaStringow():

    def __init__(self,modelform):
        self.modelform = modelform

        if modelform =="2" or modelform =="1":
            self.WartoscStringow = 700
        else:
            if  modelform =="3":
                self.WartoscStringow = 1400
            else:
                if modelform == "4":
                    self.WartoscStringow = 1400
                else:
                    if modelform == "5":
                        self.WartoscStringow = 2100
                    else:
                        if modelform == "6":
                            self.WartoscStringow = 2100
                        else:
                            if modelform == "7" or modelform == "8":
                                self.WartoscStringow = 2800
                            else:
                                self.WartoscStringow = 3500

    def count_PriceCalculationLiczbaStringow(self):
        return self.WartoscStringow