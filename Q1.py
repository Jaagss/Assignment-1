ones=["zero","one","two","thee","four","five","six","seven","eight","nine",]
tens=["twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"]
eleven=["ten","eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen","eighteen","nineteen"]
x=int(input("Enter number: "))
a=x//10 
b=x%10

#if and elif conditions for tens and ones places to check and print from the list
if a==0:
    print(ones[b])
elif a==1:
    print(eleven[b])
elif a==2:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==3:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==4:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==5:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==6:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==7:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==8:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])
elif a==9:
    if b!=0:
        print(tens[a-2]+" "+ones[b])
    else:
        print(tens[a-2])