"""calc URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from TypKlienta import views
from django.conf.urls import url
from django.contrib import admin
from django.urls import path, include
from TypKlienta.views import index,glowna,register, KalkulacjaCenowa,KalkulacjaFalownika,KalkulacjaOptymalizatory,KalkulacjaSystemMontazowy,KalkulacjaSkrzynkiAC,KalkulacjaLiczbaStringow,KalkulacjaPraceGruntowe,KalkulacjaElementyDodatkowe,KalkulacjaPPOZ,PodsumowanieBezDotacji,UlgiDotacje
from TypKlienta.views import klienciListView
from django_filters.views import FilterView
from TypKlienta.filters import KlientFilter
from django.contrib.auth import views as auth_views
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path('admin/', admin.site.urls),
    path('rozpoczeciekalkulacji/', index, name='index'),
    path('',glowna,name='glowna'),
    url(r'^klienci/$', FilterView.as_view(filterset_class=KlientFilter,template_name='TypKlienta/klienci.html'), name='klienci'),
    path("kalkulacjacenowa/", KalkulacjaCenowa, name='kalkulacjacenowa'),
    path("kalkulacjafalownika/", KalkulacjaFalownika, name='kalkulacjafalownika'),
    path("kalkulacjaoptymaliztorymocy/", KalkulacjaOptymalizatory, name='kalkulacjaoptymaliztorymocy'),
    path("kalkulacjasystemymontazowe/", KalkulacjaSystemMontazowy, name='kalkulacjasystemymontazowe'),
    path("kalkulacjaskrzynkiac/", KalkulacjaSkrzynkiAC, name='kalkulacjaskrzynkiac'),
    path("kalkulacjaliczbastringow/", KalkulacjaLiczbaStringow, name='kalkulacjaliczbastringow'),
    path("kalkulacjapracegruntowe/", KalkulacjaPraceGruntowe, name='kalkulacjapracegruntowe'),
    path("kalkulacjaelementydodatkowe/", KalkulacjaElementyDodatkowe, name='kalkulacjaelementydodatkowe'),
    path("kalkulacjappoz/", KalkulacjaPPOZ, name='kalkulacjappoz'),
    path("podsumowaniebezdotacji/", PodsumowanieBezDotacji, name='PodsumowanieBezDotacji'),
    path("kalkulacjaulgidotacje/", UlgiDotacje, name='UlgiDotacje'),
    path('register/',LoginView.as_view(template_name='TypKlienta/login.html'),name="login"),
    path('login/',LoginView.as_view(template_name='TypKlienta/login.html'),name="login"),
    path('logout/',  LogoutView.as_view(template_name='TypKlienta/logout.html'), name="login"),
    path('', include("django.contrib.auth.urls")),
    url(r'^task/(?P<pk>\d+)/remove/$', views.post_remove, name='post_remove'),

]
