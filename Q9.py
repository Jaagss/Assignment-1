import math
a,b,c,d,p=10,1.05,1,1.06,1.0

#function to return demand
def demand():
    return math.e**(a-b*p)

#function to return supply
def supply():
    return math.e**(c+d*p)

#incrementing initial price until supply crosses demand
while supply()<=demand():
    demand()
    supply()
    p+=p*0.05

print("demand:",demand(),"supply:",supply(),"price:",p)