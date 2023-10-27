num2 = tuple(map(int, input().split()))
print(num2)
reg = []
for i in num2:
    if (num2.count(i) > 1) and i not in reg:
        print(i)
        reg.append(i)