# Требуется вычислить, сколько раз встречается некоторое число X в массиве A[1..N]. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

numN = int(input("Введите количество элементов в массиве: "))

list_N = []

for i in range(numN):
    list_N.insert(i, int(input("Введите элемент массива: ")))

numX = int(input("Введите число, которое хотите проверить: "))
            
count = 0
for i in range (numN):
    if numX==list_N[i]:
        count+=1

print(f"Число {numX} встречается в массиве {count} раз(а)")
