cost=int(input("Enter cost of laptop: "))
allowance=20000
sf=0.1
r=0.005
n=0
a=allowance*sf
saving=0

#addiding allowance and rate of interest to bank until it is less than the cost of laptop
while saving<cost:
    saving+=saving*r
    saving+=a
    n+=1

print("The savings are",saving-cost)
print("The number of months are",n)
