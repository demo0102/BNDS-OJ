a = int(input())
b = int(input())
c = int(input())
if (a == b) and (b == c):
    print('equilateral triangle')
elif ((a == b) or (b == c) or (a == c)) and (((a + b) > c) and ((b + c) > a) and ((a + c) > b)):
    print('isosceles triangle')
elif ((a + b) > c) and ((b + c) > a) and ((a + c) > b):
    print('normal triangle')
else:
    print('impossible')
