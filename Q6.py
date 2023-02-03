n=int(input("Enter number of rows: "))

#Function to print the pattern
def pri(n):
    for i in range(1,n+1):
        
        for j in range(1,i+1):
            print("*",end="")
        for j in range(n-i,0,-1):
            print(" "*2,end="")
        for j in range(1,i+1):
            print("*",end="")
        
        print()

pri(n)