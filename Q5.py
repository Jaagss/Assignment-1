#function for factorial of a number
def factorial(x):
    if x==0 or x==1:
        return 1
    else:
        f=1
        for i in range(1,x+1):
            f*=i
    return f

#function to find sin
def sin(angle):
    sum=0
    for i in range(20):
        sum+=((-1)**i)*(angle**(2*i+1))/factorial((2*i+1))
    return sum

#function to find cos
def cos(angle):
    sum=0
    for i in range(20):
        sum+=((-1)**i)*(angle**(2*i))/factorial((2*i))
    return sum

#converting angle from degrees to radians
a=float(input("Enter angle : "))
a=a/180*3.14
b=float(input("Enter horizonal distance : "))

#calculating tan by dividing sin and cos
tan=sin(a)/cos(a)
h=tan*b
hypo=b/cos(a)

print("Height of pole is",h)
print("Hypotenuse is",hypo)