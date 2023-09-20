numE=int(input("Enter number: "))
sum=0
while numE!=0:
    if numE%2==0:
        sum+=numE
    numE-=1
print("Sum of Even Numbers is ", sum)