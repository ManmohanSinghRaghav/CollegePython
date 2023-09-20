import random
num=random.randrange(1,101)
while True:
    print(".\n.")
    num1=int(input("Guess Correct Number between 1 and 100\n"))
    if num==num1:
        print("Right Guess.");
        break
    elif num<num1:
        print("Too Large")
    else:
        print("Too Small")