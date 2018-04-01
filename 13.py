operator = input()
in1 = float(input())
in2 = float(input())
if operator == '+':
    print(in1 + in2)
elif operator == '-':
    print(in1 - in2)
elif operator == '*':
    print(in1 * in2)
elif in2 == 0:
    print('operation not permitted')
else:
    print(in1 / in2)
