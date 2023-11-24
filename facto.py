num1 = int(input("Enter a number: "))
def factFun(num):
    if num == 1 or num == 0:
        return 1
    return num * factFun(num-1)

print(factFun(num1))
