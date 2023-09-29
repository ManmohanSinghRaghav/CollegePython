str=input('Enter TEXT: ')
vow='aeiou'
Num_vow=0
Num_con=0
Num_digi=0
Num_spc=0
for i in str:
    if i.lower() in vow:
        Num_vow+=1
    elif i.isalpha() and i.lower() not in vow:
        Num_con+=1
    elif i.isdigit():
        Num_digi+=1
    elif i.isspace():
        Num_spc+=1
    else:
        pass;
print(f"Total number of vowels: {Num_vow}")
print(f"Total number of consonants: {Num_con}")
print(f"Total number of digits: {Num_digi}")
print(f"Total number of White Spaces: {Num_spc}")