from datetime import datetime

from django.db import models

datetime.now()
class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class TypKlienta(BaseModel):

    def __str__(self):
        return self.nazwa + " "

    nazwa = models.CharField(max_length=100, null=False,unique=True)


    class Meta:
        verbose_name = "Typ klienta"
        verbose_name_plural = "Typ klienta"

class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True

class klient(BaseModel):

    def __str__(self):
        return self.imie + " " + self.nazwisko + " " + self.ulica


    IdKlienta = models.AutoField(primary_key=True)
    data =  models.DateTimeField(default=datetime.now)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    ulica = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    telefon = models.CharField(max_length=11)
    typ = models.ForeignKey(TypKlienta, to_field='nazwa',null=True, on_delete=models.CASCADE)
    metraz = models.IntegerField()
    zuzycie = models.IntegerField()

    class Meta:
        verbose_name = "Klient"
        verbose_name_plural = "Klient"

class Vat(BaseModel):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)
    wartosc = models.DecimalField(max_digits=100, decimal_places=2)
    Vat_id = models.ForeignKey(TypKlienta, null=True, on_delete=models.CASCADE)

    class Meta:
        verbose_name = "Vat"
        verbose_name_plural = "Vat"
class KadNachyleniaDachu(BaseModel):
    def __str__(self):
        return self.kadnachylenia

    kadnachylenia = models.CharField(max_length=100)
    przelicznik = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Kąt nachylenia dachu"
        verbose_name_plural = "Kąt nachylenia dachu"

class EkspozycjaDachowa(BaseModel):
    def __str__(self):
        return self.ekspozycja

    ekspozycja = models.CharField(max_length=100)
    mnoznik = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Ekspozycja dachowa"
        verbose_name_plural = "Ekspozycja dachowa"