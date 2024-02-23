def AreaOfTrapezoid(a, b, h):
    return (a + b)/2 * h

a = int(input("Base1: "))
b = int(input("Base2: "))
h = int(input("Height: "))

print("Area of trapezoid: ",AreaOfTrapezoid(a, b, h))