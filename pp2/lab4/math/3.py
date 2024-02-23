import math

def Area(n, l):
    p = (n * l) * 0.5
    a = l / 2 * math.tan(math.pi/n)
    return math.ceil(p * a)

n = int(input("Number of sides: "))
l = int(input("Length of a side: "))
print("The area of the polygon is: ", Area(n, l))