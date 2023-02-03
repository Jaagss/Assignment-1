import math
a=float(input("Enter start time: "))
b=float(input("Enter end time: "))
t=a
f,d=0,0

def function(t):
    return 2000*math.log(140000/(140000-(2100*t))) - (9.8*t)

#adding the speed at different time
while t<b:
    avg=(function(t)+function(t+0.25))/2
    d+=avg*0.25
    t+=0.25

print(d)
