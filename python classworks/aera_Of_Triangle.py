x1 = float(input('Enter a number x1: '))
y1 = float(input('Enter a number y1: '))
x2 = float(input('Enter a number x2: '))
y2 = float(input('Enter a number y2: '))
x3 = float(input('Enter a number x3: '))
y3 = float(input('Enter a number y3: '))
side1 = ((x2-x1)**2+(y2 -y1)**2)**0.5;
side2 = ((x3-x2)**2+(y3-y2)**2)**0.5;
side3 = ((x1-x3)**2+(y1-y3)**2)**0.5;
side = (side1+side2+side3)/2;
area = (side*(side-side1)*(side-side2)*(side-side3))**0.5;
print(area)
