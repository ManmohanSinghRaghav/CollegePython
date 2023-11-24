def IsEven(num):
    return True if num%2==0 else False
num1 = int('Enter a Number : ')
print(f"{num1} is", "an Even" if IsEven(num1) else "a Odd", "number")