dict1={
    'english': 118,
    'physics': 112,
    'maths': 112,
    'aiml': 214,
    'webtech': 218,
    }
sum = 0
for i in dict1.values():
    if type(i)==int:
        sum+=i
print(sum)