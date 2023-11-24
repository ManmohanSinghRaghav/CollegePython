def area(length,breadth):
    return length*breadth

def peri(length,breadth):
    return 2*(length+breadth)

ls = int(input("Enter the length : "))
bs = int(input("Enter the breadth : "))
area_ = area(ls, bs)
peri_ = peri(ls, bs)
print(f"Area of rectangle : {area_}\nPerimeter of rectangle : {peri_}")


