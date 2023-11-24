def listSort(ls):
    ls_a = sorted(ls)
    ls_d = sorted(ls, reverse=True)
    return 1 if ls==ls_a else 0 if ls_d == ls else -1

lst = [7,6,5,4,3]
print(listSort(lst))