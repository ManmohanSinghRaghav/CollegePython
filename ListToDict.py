lst1 = ['Maths', 'Physics', 'Python']
lst2 = [132, 213, 134]
dict1={}
dict2=dict(zip(lst1,lst2))
# OR
for i in range(len(lst1)):
    dict1.update({lst1[i]: lst2[i]})

print(dict1,'\n',dict2)

