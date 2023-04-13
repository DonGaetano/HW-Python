# Напишите рекурсивную функцию sum(a, b), возвращающую сумму двух целых неотрицательных чисел. 
# Из всех арифметических операций допускаются только +1 и -1. 
# Также нельзя использовать циклы.

def sum_numbers(a,b):
    if a == 0 and b == 0:
        return 0
    if a > 0:
        return sum_numbers(a-1,b) + 1
    if b > 0:
        return sum_numbers(a,b-1) + 1

number_A = int(input("Введите целое неотрицательное число A: "))
number_B = int(input("Введите целое неотрицательное числа B: "))
print(f"{number_A} + {number_B} = {sum_numbers(number_A, number_B)}")
