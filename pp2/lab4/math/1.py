import math

def toRadian(degree):
    return degree * math.pi/180

degree = int(input("Degree: "))
print(toRadian(degree))