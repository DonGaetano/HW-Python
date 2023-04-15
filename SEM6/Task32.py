# Определить индексы элементов массива (списка), значения которых принадлежат заданному диапазону 
# (т.е. не меньше заданного минимума и не больше заданного максимума)

def fill_the_list(a, list):
    list = []
    for i in range(a):
        list.insert(i, int(input("Введите элемент массива: ")))
    return list

def match_the_range(b, c, list):
    for i in range(len(list)):
        if b <= list[i] <= c:
            print(f"Элемент под индексом {i} находится в границах заданного диапазона")

number_A = int(input("Введите количество элеменетов массива: "))
number_B = int(input("Введите минимальную границу диапазона: "))
number_C = int(input("Введите максимальную границу диапазона: "))

list_range = []
print(fill_the_list(number_A, list_range))
match_the_range(number_B, number_C, list_range)
