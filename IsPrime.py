num=int(input("Enter Number: "))
i=2
while i!=num:
    if num//i==0:
        print(i)
        print(num,'is not Prime.')
        break
    i+=1
else:
    print(num,'is Prime.')