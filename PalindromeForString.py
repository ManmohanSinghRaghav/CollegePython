char1=input("Enter Text: ")

char2=char1[len(char1)-1::-1]

if char1==char2:
    print(char1, 'is Palindrome.')
else:
    print(char1, 'is not Palindrome.')
    

    

    