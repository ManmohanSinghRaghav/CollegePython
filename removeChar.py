str=input('Enter a String: ')
str1=''
for i in str:
    if i.isalpha():
        str1+=i
print(str1)