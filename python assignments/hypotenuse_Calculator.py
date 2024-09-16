import math

def pythagoras(side1, side2):
    return (side1**2 + side2**2)**0.5
side1 = 3
side2 = 4
hypotenuse = pythagoras(side1, side2)
print(f"The length of the hypotenuse is: {hypotenuse:.2f}")
