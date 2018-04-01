weight = float(input())
height = float(input())
bmi = weight / (height**2)
if bmi < 18:
    print('too thin')
elif bmi <= 25:
    print('very good')
elif bmi < 30:
    print('overweight')
elif bmi < 35:
    print('fat')
elif bmi < 40:
    print('normal fat')
else:
    print('too fat')
