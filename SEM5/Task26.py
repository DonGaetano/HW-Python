# Напишите программу, которая на вход принимает два числа A и B, и возводит число А в целую степень B с помощью рекурсии.

def involution(a,b):
    result = 1
    if b == 0:
        return result
    else:
        for i in range(1, b+1):
            result *=a
        return result

number_A = int(input("Введите число A: "))
number_B = int(input("Введите степень числа A: "))
print(f"{number_A} в степени {number_B} = {involution(number_A, number_B)}")
