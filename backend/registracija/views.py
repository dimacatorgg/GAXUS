from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import uuid
from .models import User
import backend.neo4jkonekcija as neo
def home(requests):
    return HttpResponse(f"{requests.GET.get("ime")}")

def registrujga(requests):
    name = requests.GET.get("name","jebiga")
    password = requests.GET.get("password","jebiga")
    kmail = requests.GET.get("gmail","jebiga")
    id = str(uuid.uuid4())
    if(neo.getdata(name) or neo.getdata(kmail)  or requests.COOKIES.get("idx")!=""):
        return HttpResponse("Vec postji takav korsnik ili ste prijavljeni")
    else:
        neo.ikok(name,password,kmail,id)
    res= JsonResponse({'message':f'Uspesno ste ste ulogovali {requests.COOKIES.get("idx")}'})
    res.set_cookie("idx",id,max_age=100000)
   
    
    return res
    
def gug(requests):
    return JsonResponse({"message":f"{requests.GET.get("podatak",":s")}"})
def nes(requests):
    return JsonResponse({"message":"sdadasdsadasd"})
def dajmu_kuki(requests):
    kolacic = requests.COOKIES.get("idx"," ")
    return JsonResponse({"message":f"{kolacic}"})

def dd(requests):
    res = JsonResponse({"message":"Kuki izbrisan"})
    res.delete_cookie("idx")
    return res
def lol(requests):
    
    return HttpResponse(neo.getdata(requests.COOKIES.get("idx")) + f"   {requests.COOKIES.get("idx")}")
    #nesto = neo.getdata(requests.COOKIES.get("name"))
    #return JsonResponse({"message":f"{nesto} kolacijc je {requests.COOKIES.get("name")}"})