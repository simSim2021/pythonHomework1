# Задание 2.1.
# Шестизначный автобусный билет считается удачным, если сумма его цифр делится на 7.
# Могут ли два билета подряд быть удачными?

def dignum(n):
    aaa = 0
    while n > 0:
        dig = n % 10
        aaa += dig
        n = n//10
    return aaa


for i in range(1000000):
    if dignum(i) % 7 == 0 and dignum(i+1) % 7 == 0:
        print(i, i+1)




