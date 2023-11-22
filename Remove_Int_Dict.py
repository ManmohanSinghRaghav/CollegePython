dict1={
    'english': 118,
    'physics': 112,
    'maths': 112,
    'aiml': 218,
    'webtech': 218,
    'python': None
    }
for i,j in list(dict1.items()):
    if type(j)!=int:
        dict1.pop(i)
print(dict1)