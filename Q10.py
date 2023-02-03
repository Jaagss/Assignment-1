x=float(input("Enter x : "))

#function for polynomial
def poly(x):
    return x**3-10.5*x**2+34.5*x-35

#function derivative
def p(x):
    return 3*x**2-21*x+34.5

#finding roots and printing it 
while True:
    if poly(x)>=-0.2 and poly(x)<=0.2:
        print(x)
        break
    else:
        a=x-poly(x)/p(x)
        x=a