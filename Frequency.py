ch=input('Enter TXT: ')
reg=''
for j in ch:
    count=0
    if j not in reg:
        for i in ch:
            if i==j:
                count+=1
        print(j,':',count)
        reg+=j