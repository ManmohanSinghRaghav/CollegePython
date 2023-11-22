dict1={
    'english': 118,
    'physics': 112,
    'maths': 112,
    'aiml': 218,
    'webtech': 218,
    }
max_m = max(dict1.values())
min_m = min(dict1.values())
sub_max = []
sub_min = []
for i, j in dict1.items():
    if j == max_m:
        sub_max.append(i)
    elif j == min_m:
        sub_min.append(i)
print('Maximum: ',sub_max, max_m)
print('Minimum: ',sub_min, min_m)