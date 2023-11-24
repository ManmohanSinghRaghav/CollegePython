def listSort(ls):
    for i in ls:
        if type(i)!=int:
            return False
    return True

lst = [7,6,5,4,3]
print(listSort(lst))