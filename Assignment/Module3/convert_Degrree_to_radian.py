import math

def degree_to_radian():
    degree = float(input("Enter a degree value: "))
    radian = math.radians(degree)
    print (f"The radian value of {degree} degrees is {radian} radians.")

degree_to_radian()