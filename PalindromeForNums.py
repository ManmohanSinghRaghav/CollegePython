num=int(input('Enter number: '))
n=num
check=0
while n!=0:
    check*=10
    check+=n%10
    n=n//10
if check==num:
    print(num,'is equal to',check)
    print(num, 'is Palindrome.')
else:
    print(num,'is not equal to',check)
    print(num, 'is not Palindrome.')
    