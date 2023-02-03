x=0
M=int(input("Enter number of iterations : "))

#finding the roots of both equations
while True:
    eq1=120-2*x
    eq2=(400-8*x)/2
    if eq1==eq2:
        print("Number of tables: ",x)
        print("Number of chairs: ",eq1)
        break
    else:
        x+=1

#determining the profit from the number of iterations
def profit(M,x):
    if M>x:
        return (M*90+M*25)
    else:
        return (M*90+M*25+(x-M)*100+(x-M)*30)

print("Profit is",profit(M,x))