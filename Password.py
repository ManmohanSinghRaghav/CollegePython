pass1="Manmohan(1)"
time=0
while time!=3:
    pass2=input("Confirm Password: ")
    if pass1==pass2:
        print(">>> Correct Password.")
        break
    else:
        print(">>> Wrong Password.")
        print("...Try Again...")
        time+=1
else:
    print("Wrong Password.")
    print(".\n.\n.\n---TIMEOUT---")