a = int(input())
b = int(input())
c = int(input())
# $ax^2 + bx + c = 0$
delta = b**2 - 4*a*c
if a == 0:
    print('one answer')
elif delta < 0:
    print('no answer')
elif delta == 0:
    print('two equal answers')
else:
    print('two answers')
