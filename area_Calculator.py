# Time to make a app that can find the area of an regular shape.
input("Welcome to the area calculator. Press any Key to Continue.")
print("In this calculator you can calculate the area of circle, Parallelogram, Square, Rectangle, Rhombus, Trapezium.")
z = input("Which surface do you want to choose to find the area? \n")
z = z.lower()
if z == "parallelogram":
    base = input("Please Enter Base: ")
    height = input("Please Enter Height: ")
    area_of_parallelogram = int(base)*int(height)
    print("Area of parallelogram is",area_of_parallelogram,"sq.m")
elif z == "circle":
    radius = input("Please Enter Radius: ")
    area_of_circle = 22/7*int(radius)**2
    print("Area of circle is",area_of_circle,"sq.m")
elif z == "square":
    l = input("Please Enter Length: ")
    area_of_square = int(l)**2
    print("Area of square is",area_of_square,"sq.m")
elif z == "rectangle":
    Length = input("Enter Length: ")
    Breadth = input("Enter Breadth:")
    area_of_rectangle = int(Length)*int(Breadth)
    print("Area of rectangle is",area_of_rectangle,"sq.m")
elif z == "rhombus":
    d1 = input("Enter diagonal1: ")
    d2 = input("Enter diagonal2: ")
    area_of_rhombus = 1/2*int(d1)*int(d2)
    print("Area of rhombus is",area_of_rhombus,"sq.m")
elif z == "trapezium":
    h = input("Enter The Height: ")
    a = input("Enter l1: ")
    b = input("Enter l2: ")
    area_of_trapezium = 1/2*(int(h)*int(a)+int(h)*int(b))
    print("Area of Trapezium is",area_of_trapezium,"sq.m")
else:
    print("This program only calculates the area of circle, Parallelogram, Square, Rectangle, Rhombus, Trapezium. ")
input("Press any Key to exit: ")
