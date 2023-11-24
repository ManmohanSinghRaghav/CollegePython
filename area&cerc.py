def area(radius):
    return 3.14*(radius**2)

def circum(radius):
    return 2*3.14*radius

rs = int(input("Enter the radius : "))
area_ = area(rs)
circum_ = circum(rs)
print(f"Area of Circle: {area_}\ncircumference of Circle: {circum_}")


