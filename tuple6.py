num = [(10,20,40), (40,50,60), (70,80,90)]
for i in range(0,len(num)):
    num1 = list(num[1])
    num1.pop()
    num1.append(100)
    num[i] = tuple(num1)
print(num)
