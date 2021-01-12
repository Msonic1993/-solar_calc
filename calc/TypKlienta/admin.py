from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .models import TypKlienta, Vat, KadNachyleniaDachu, EkspozycjaDachowa, klient, MarzaFirmy,Profile

# Register your models here.

admin.site.register(klient)
admin.site.register(TypKlienta)
admin.site.register(Vat)
admin.site.register(KadNachyleniaDachu)
admin.site.register(EkspozycjaDachowa)
admin.site.register(MarzaFirmy)
admin.site.register(Profile)

class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)