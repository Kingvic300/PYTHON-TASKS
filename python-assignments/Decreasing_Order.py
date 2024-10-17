print('Enter three number.')
digit1 = int(input('Enter the first number:'))
digit2 = int(input('Enter the second number:'))
digit3 = int(input('Enter the second number:'))
if digit1 > digit2 and digit2 > digit3:
    if digit2 > digit3:
        print(digit1,digit2,digit3)
    else:
        print(digit1,digit3,digit2)
elif digit2 > digit1 and digit2 > digit3:
    if digit1 > digit3:
        print(digit2,digit1,digt3)
    else:
        print(digit2,digit3,digit1)
else:
    if digit1 > digit2:
        print(digit3,digit1,digit2)
    else:
        print(digit3,digit2,digit1)  
        
