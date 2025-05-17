from random import randint
podaci = [1,2,3]
sigma = []
dobro = 0
for hej in range(10):
    i = randint(0,10)
    for gg in podaci:
        if(gg==i):
            dobro+=1
        else:
            dobro-=1
    
    for r in range(len(podaci)):
        if(r==len(podaci)-1):
            podaci[0] = i
            break
        else:
            sigma.append([podaci[r],r+1])
    for j in range(len(sigma)):
        podaci[sigma[j][1]] = sigma[j][0]
    print(podaci)
print(dobro)
