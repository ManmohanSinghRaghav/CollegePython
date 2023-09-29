str=input('enter string: ')
count=0
for i in str:
    count+=1
print('Length of String using loop: ',count,'; using len() function: ',len(str))