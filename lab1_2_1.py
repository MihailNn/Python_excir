#Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
#Могут ли два билета подряд быть удачными?

sumNum = 0
for i in range(100000, 999999):
    num = [int(d) for d in str(i)]
    numPlus = [int(d) for d in str(i+1)]
    sumNum = sum(num)
    sumNumPlus = sum(numPlus)
    if sumNum % 7 == 0 and sumNumPlus % 7 == 0:
        print(num, numPlus)