from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
from .models import User

def home(requests):
    return HttpResponse(f"{requests.GET.get("ime")}")

def registrujga(requests):
    name = requests.GET.get("name","jebiga")
    password = requests.GET.get("password","jebiga")
    kmail = requests.GET.get("gmail","jebiga")
    
    
    res= JsonResponse({'message':f'Uspesno ste ste ulogovali {user.name}'})
    res.set_cookie("name",user.name,max_age=100000)
    user = User(name=name,password=password,gmail=kmail)
    user.save()
    
def gug(requests):
    return JsonResponse({"message":f"{requests.GET.get("podatak",":s")}"})
def nes(requests):
    return JsonResponse({"message":"sdadasdsadasd"})
def dajmu_kuki(requests):
    kolacic = requests.COOKIES.get("user"," ")
    return JsonResponse({"message":f"{kolacic}"})
def dd(requests):
    res = HttpResponse(f"{requests.COOKIES.get("user")}")
    res.delete_cookie("user")
    return res