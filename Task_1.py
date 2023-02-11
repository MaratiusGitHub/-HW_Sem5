# Задача 26:  Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую
# степень B с помощью рекурсии.
# A = 3; B = 5 -> 243 (3⁵)
# A = 2; B = 3 -> 8

a = int(input('Введите число: '))
b = int(input('введите степень: '))

def power(num, step):
    x = num
    if step == 1:
        return num
    return x * power(num, step - 1)

print(power(a, b))
