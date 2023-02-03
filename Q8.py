pop=[50,1450,1400,1700,1500,600,1200]
y=0
g1,g2,g3,g4,g5,g6,g7=2.5/100,2.1/100,1.7/100,1.3/100,0.9/100,0.5/100,0.1/100
tot_pop=0
n=0

#function to calculate the lenght of list
def l(pop):
    c=0
    for i in pop:
        c+=1
    return c

#calculating total population in the list
for i in pop:
    tot_pop+=i
print("Current population is",tot_pop)

#changing poplation according to growth factor
while True:
    sum=0
    for i in range(l(pop)):
        if i==0:
            pop[i]+=pop[i]*g1
        elif i==1:
            pop[i]+=pop[i]*g2
        elif i==2:
            pop[i]+=pop[i]*g3
        elif i==3:
            pop[i]+=pop[i]*g4
        elif i==4:
            pop[i]+=pop[i]*g5
        elif i==5:
            pop[i]+=pop[i]*g6
        elif i==6:
            pop[i]+=pop[i]*g7
    g1-=0.1/100
    g2-=0.1/100
    g3-=0.1/100
    g4-=0.1/100
    g5-=0.1/100
    g6-=0.1/100
    g7-=0.1/100
    n+=1
    for i in pop:
        sum+=i
    if tot_pop>=sum:
        break
    else:
        tot_pop=sum

print("The population is",tot_pop)
print("Number of years are",n-1)

