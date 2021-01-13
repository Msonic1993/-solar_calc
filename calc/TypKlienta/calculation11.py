from TypKlienta.models import klient, MarzaFirmy, MarzaHandlowca
from decimal import Decimal






class PodsumowanieBezDotacjiCalc():
    WartoscModulowStr = klient.objects.last().WartoscModulow
    WartoscFalownikowStr = klient.objects.last().WartoscFalownikow
    WartoscOptyalizatorowStr = klient.objects.last().WartoscOptymalizatorow
    WartoscSystemuMontazowegoStr = klient.objects.last().WartoscSystemuMontazowego
    WartoscSkrzynekACStr = klient.objects.last().WartoscSkrzynekAC
    WartoscStringowStr = klient.objects.last().WartoscStringow
    WartoscOkablowaniaACStr = klient.objects.last().WartoscOkablowaniaAC
    WartoscOkablowaniaDCStr = klient.objects.last().WartoscOkablowaniaDC
    KosztTransportuStr = klient.objects.last().KosztTransportu
    KosztMontazuStr = klient.objects.last().KosztMontazu
    KosztPracGruntowychStr = klient.objects.last().KosztPracGruntowych
    KosztWiFiExtenderStr = klient.objects.last().KosztWiFiExtender
    KosztZwyszkaStr = klient.objects.last().KosztZwyszka
    KosztPPOZStr = klient.objects.last().KosztPPOZ
    MarzaFirmyStr = MarzaFirmy.objects.get(id=1).WartoscMarzy
    MarzaHandlowcaStr = MarzaHandlowca.objects.get(KamId=2).WartoscMarzy
    MocModulowStr = klient.objects.last().MocInstalacji
    TypKilentaStr = klient.objects.last().typ_id
    MetrazStr = klient.objects.last().metraz
    UlgaMojPrad = klient.objects.last().MojPrad


    def __init__(self):

        self.PodsumowanieWynik1=  self.WartoscModulowStr + self.WartoscFalownikowStr + self.WartoscSystemuMontazowegoStr + self.WartoscSkrzynekACStr +self.WartoscStringowStr + self.WartoscOkablowaniaACStr +self.WartoscOkablowaniaDCStr +self.KosztTransportuStr +self.KosztMontazuStr +self.KosztWiFiExtenderStr + self.KosztZwyszkaStr + self.KosztPPOZStr
        self.PodsumowanieWynik2 = self.PodsumowanieWynik1 / (1-self.MarzaFirmyStr)
        self.PodsumowanieWynik = self.PodsumowanieWynik2 + (self.MarzaHandlowcaStr * self.MocModulowStr)

        if  self.TypKilentaStr == "indywidualny" and self.MetrazStr <= 300:
            self.PodsumowanieWynikBrutto = float(self.PodsumowanieWynik) * 0.08 + float(self.PodsumowanieWynik)- self.UlgaMojPrad

        else:
            if self.TypKilentaStr == "indywidualny" and self.MetrazStr > 300:
               self.PodsumowanieWynikBrutto = float(self.PodsumowanieWynik) * 0.23 + float(self.PodsumowanieWynik)- self.UlgaMojPrad
            else:
                if self.TypKilentaStr == "Biznesowy":
                   self.PodsumowanieWynikBrutto = float(self.PodsumowanieWynik) * 0.23 + float(self.PodsumowanieWynik) - self.UlgaMojPrad
                else:
                   if self.TypKilentaStr == "Rolnik - gospodarstwa domowego" and self.MetrazStr <= 300:
                       self.PodsumowanieWynikBrutto = float(self.PodsumowanieWynik) * 0.08 + float(self.PodsumowanieWynik)- self.UlgaMojPrad
                   else:
                       if self.TypKilentaStr == "Rolnik - gospodarstwa domowego" and self.MetrazStr > 300:
                           self.PodsumowanieWynikBrutto = float(self.PodsumowanieWynik) * 0.23 + float( self.PodsumowanieWynik)- self.UlgaMojPrad
                       else:
                           self.PodsumowanieWynikBrutto = float(self.PodsumowanieWynik) * 0.23 + float(self.PodsumowanieWynik)- self.UlgaMojPrad




    def count_PodsumowanieBezDotacjiCalc(self):
         return round(self.PodsumowanieWynik,2), round(self.PodsumowanieWynikBrutto,2)
