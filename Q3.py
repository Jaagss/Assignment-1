x0,y0=5.0,5.0
n,s,w,e,disth,distb=0,0,0,0,0,0

#Placing conditons and adding the distance to the specific direction
while True:
    x=int(input("Enter Distance: "))
    if x<=0:
        break
    elif x<=25:
        n+=x
    elif x>=26 and x<=50:
        s+=x
    elif x>=51 and x<=75:
        e+=x
    elif x>=76:
        w+=x

#creating variables for displacement,total distance,etc
distv=n-s
distb=e-w
disp=abs(((distv)**2)+((distb)**2))**(1/2)
dist=n+s+w+e

print("Final Coordinates:",distb+x0,",",distv+y0)
print("Total Distance:",dist)
print("Displacement:",disp)