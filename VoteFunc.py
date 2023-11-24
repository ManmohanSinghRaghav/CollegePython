def vote(age):
    if age >= 18 :
        return True
    else:
        return False

age_ = int(input('Enter Your Age : '))
if vote(age_):
    print(f"Yes, You can Vote.")
else:
    print(f"No, You can not vote")