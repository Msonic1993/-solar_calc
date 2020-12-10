from datetime import datetime
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

datetime.now()
class BaseModel(models.Model):
    objects = models.Manager()
    class Meta:
        abstract = True


class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField(max_length=500, blank=True)
    is_confirmed = models.BooleanField(default=False)


@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)


@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()


class Friendship(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, related_name="friendship_creator_set", on_delete=models.CASCADE)
    friend = models.ForeignKey(User, related_name="friend_set", on_delete=models.CASCADE)


class Blocking(models.Model):
    created = models.DateTimeField(auto_now_add=True, editable=False)
    creator = models.ForeignKey(User, related_name="blocking_creator_set", on_delete=models.CASCADE)
    blocked = models.ForeignKey(User, related_name="blocked_set", on_delete=models.CASCADE)



class KadNachyleniaDachu(BaseModel):
    def __str__(self):
        return self.kadnachylenia

    kadnachylenia = models.CharField(max_length=100)
    przelicznik = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Kąt nachylenia dachu"
        verbose_name_plural = "Kąt nachylenia dachu"

class Moduly(BaseModel):
    def __str__(self):
        return str(self.model)

    producent = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    moc = models.DecimalField(max_digits=100, decimal_places=3, null=True)
    cenanetto = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    cenabrutto = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Moduły fotowoltaiczne"
        verbose_name_plural = "Moduły fotowoltaiczne"


class Falowniki(BaseModel):
    def __str__(self):
        return str(self.model)

    producent = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cenanetto = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    cenabrutto = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Falowniki"
        verbose_name_plural = "Falowniki"


class Optymalizatory(BaseModel):
    def __str__(self):
        return self.model

    producent = models.CharField(max_length=100)
    model = models.CharField(max_length=100)
    cenanetto = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    cenabrutto = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Optymalizatory"
        verbose_name_plural = "Optymalizatory"

class Systemumontazowe(BaseModel):
    def __str__(self):
        return self.nazwa

    nazwa = models.CharField(max_length=100)
    cenanetto = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    cenabrutto = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Optymalizatory"
        verbose_name_plural = "Optymalizatory"


class EkspozycjaDachowa(BaseModel):
    def __str__(self):
        return self.ekspozycja

    ekspozycja = models.CharField(max_length=100)
    mnoznik = models.DecimalField(max_digits=100, decimal_places=2, null=True)

    class Meta:
        verbose_name = "Ekspozycja dachowa"
        verbose_name_plural = "Ekspozycja dachowa"

class  WymaganaMocInstalacji(BaseModel):
    def __str__(self):
        return str(self.WymaganaMoc)

    IdKlienta = models.DecimalField(max_digits=100, decimal_places=2, null=True)
    WymaganaMoc = models.DecimalField(max_digits=100, decimal_places=2, null=True)


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
        return str(self.typ) +  str(self.ekspozycjaDachowa)+  str(self.kadNachyleniaDachu) + str(self.WymaganaMoc)

    IdKlienta = models.AutoField(primary_key=True)
    data =  models.DateTimeField(default=datetime.now)
    imie = models.CharField(max_length=20)
    nazwisko = models.CharField(max_length=30)
    ulica = models.CharField(max_length=100)
    miasto = models.CharField(max_length=100)
    telefon = models.CharField(max_length=11)
    typ = models.ForeignKey(TypKlienta, to_field='nazwa',null=True, on_delete=models.CASCADE)
    ekspozycjaDachowa =  models.ForeignKey(EkspozycjaDachowa, null=True, on_delete=models.CASCADE)
    kadNachyleniaDachu = models.ForeignKey(KadNachyleniaDachu, null=True, on_delete=models.CASCADE)
    metraz = models.IntegerField(null=False)
    zuzycie = models.IntegerField(null=False)
    WymaganaMoc = models.ForeignKey(WymaganaMocInstalacji, null=True, on_delete=models.CASCADE)
    KamId = models.ForeignKey(User, null=True, on_delete=models.CASCADE)



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





