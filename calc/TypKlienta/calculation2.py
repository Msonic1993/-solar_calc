class PriceCalculation():



    def __init__(self,MocModulu,SugerowanaMoc1,LiczbaModulow,model):

        self.MocModulu = MocModulu
        self.model = model
        self.SugerowanaMoc = SugerowanaMoc1
        self.LiczbaModulow = LiczbaModulow


        if model:

            self.LiczbaModulow = SugerowanaMoc1 / MocModulu
        else:
            self.LiczbaModulow = SugerowanaMoc1

    def count_PriceCalculation(self):
        return self.LiczbaModulow