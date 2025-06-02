"""
URL configuration for backend project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.contrib import admin
from django.urls import path
from registracija import views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name="home"),
    path('api/register/',views.registrujga,name="registrujga"),
    path('api/test/',views.nes,name='nes'),
    path('api/ses/',views.gug,name="sdasdsad"),
    path('api/cockie/',views.dajmu_kuki,name="sdasdasdada"),
    path('api/cockied/',views.dd,name="sdas"),
    path('api/kuki/',views.dd,name="sdasd"),
    path('api/lol/',views.lol,name="sadasd"),
    path('api/login/',views.login,name="Mjaju"),
    path('test/',views.test,name="sdad"),
    path('api/prijatelj/',views.prijatelj,name="dasdasdasd"),
    path('api/add/',views.addd,name="sdasd"),
    path('api/prijateljd/',views.hju,name="dsada"),
    path('api/ty/',views.tyes,name="sdasd"),
    path('api/del/',views.delg,name="sdasd"),
    path('api/sigma/',views.sigma,name="sdasda"),
    path('api/check/',views.prvoeri,name="Nesto"),
    path('api/ntest/',views.novitest,name="Nesto"),
    path('api/nntest/',views.nntest,name="sdsd"),
    path('api/verify/',views.sentmail,name="sasdasdasdasdasdasdasdasdasd"),
    path('api/anout/',views.about,name="Sdasdasdasdada")
]
