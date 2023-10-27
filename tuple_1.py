num = [(), (), ('',), ('a','b'), ('a','b','c'), ('d')]
for i in range(num.count(())):
    num.remove(())
print(num)