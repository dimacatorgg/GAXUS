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
    if(neo.proveri(name,kmail)):
        return JsonResponse({"message":"Vec postji ili ime ili mjl koji korsits"})
    else:
        neo.ikok(name,password,kmail,id)
        res = JsonResponse({"message":f"{requests.COOKIES.get("idx")}"})
        res.set_cookie("idx",id)
        
        return res
    
def gug(requests):
    return JsonResponse({"message":f"{requests.GET.get("podatak",":s")}"})
def nes(requests):
    return JsonResponse({"message":"sdadasdsadasd"})
def dajmu_kuki(requests):
    kolacic = requests.COOKIES.get("idx","")
    print(kolacic)
    return JsonResponse({"message":f"{kolacic}"})

def dd(requests):
    res = JsonResponse({"message":"Kuki izbrisan"})
    res.delete_cookie("idx")
    return res
def lol(requests):
    
    return HttpResponse(neo.getdata(requests.COOKIES.get("idx")))
    #nesto = neo.getdata(requests.COOKIES.get("name"))
    #return JsonResponse({"message":f"{nesto} kolacijc je {requests.COOKIES.get("name")}"})
def login(requests):
    ime = requests.GET.get("name")
    pas = requests.GET.get("password")
    od = neo.proverin(ime,pas)
    res = ""

    if(od):
        res = JsonResponse({"message":neo.dobijid(ime)})
        res.set_cookie("idx",neo.dobijid(ime))
        print("Hej")
        return res
    else:
        print("hej")
        return JsonResponse({"message":"Nema takovg naloga"})
   
def test(requests):
    nesto = requests.GET.get("id")
    print(neo.uzmisvepodtke(nesto))
    return JsonResponse({"message":neo.uzmisvepodtke(nesto)})
def prijatelj(requests):
    ime = requests.GET.get("ime")
    return JsonResponse({"message":neo.prijatelji(ime)})
def addd(requests):
    user1 = requests.GET.get("user1")
    user2 = requests.GET.get("user2")
    res = neo.friendadd(user1,user2)
    print(res)
    return JsonResponse({"message":"sad"})
def hju(requests):
    ju = requests.GET.get("user")
    return JsonResponse({"message":neo.prijatelj(ju)})
def tyes(requests):
    u1 = requests.GET.get("user1")
    u2 = requests.GET.get("user2")
    return JsonResponse({"message":neo.dodaj(u1,u2)})
def delg(requests):
    u1 = requests.GET.get("user1")
    u2 = requests.GET.get("user2")
    neo.delete(u1,u2)
    return JsonResponse({'message':'uradjeno'})