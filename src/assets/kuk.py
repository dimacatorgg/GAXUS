from random import randint
def generisati(n):
    gug = []
    for i in range(n):
        gug.append(randint(-50,50))
    return gug
def test(lista):
    a,b,c = 0,0,0
    for i in lista:
        if(i>0):
            a+=1
        elif(i<0):
            b+=1
        else:
            c+=1
    print("Ima ",a,"pozitivnih brojeva")
    print("Ima",b,"negativnih brojeva")
    print("Ima",c,"nula")
gog = generisati(5)
test(gog)
#drugi zadatak
def gge(g):
    gug = []
    for i in range(g):
        gug.append(randint(0,50))
    return gug
kuk = gge(5)
def nesto(kik):
    h,t = 0,0
    arim = []
    for i in kik:
        if(i%2==0):
            h+=1
            t+=i
            arim.append(i)
    return h,t,(sum(arim)/len(arim))
hej,hoj,hij = nesto(kuk)
print("Ima",hej,"parnih brojeva",hoj,"je zbir parnih brojvea i nhjiva artiemticka sredije",hij)
def temperatura(h):
    gk = []
    for i in range(h):
        gk.append(randint(1,30))
    return gk
def ggi(gi):
    ok = 0
    avg = sum(gi)/len(gi)
    for i in gi:
        if(avg<i):
            ok+=1
    return ok,avg
some = temperatura(5)
pk,pa = ggi(some)
print(some)
print("Imac n dana izand proseka",pk,"avg je pa",pa)
jupi = generisati(8)
def hig(jug):
    jus = jug
    for i in range(len(jus)):
        if(jus[i]<0):
            jus[i] = 0
    return jus
print(jupi)
print(hig(jupi))
brojevi = input().split()
rezultat = []

for i in range(len(brojevi)):
    if i % 2 != 0:
        rezultat.append(int(brojevi[i]))

print(rezultat)
print(len(rezultat))
print(sum(rezultat))
A = []

n = int(input("Unesite broj elemenata: "))

for i in range(n):
    A.append(int(input("Unesite element: ")))

B = []

for broj in A:
    B.append(broj ** 2)

print(B)

