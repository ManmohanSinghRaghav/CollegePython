n=int(input("Enter Number: "))
a=0
b=1
sum=0
while n!=0:
    print(a, end=" ")
    sum=a+b
    a=b
    b=sum
    n-=1