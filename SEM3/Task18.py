# Требуется найти в массиве A[1..N] самый близкий по величине элемент к заданному числу X. 
# Пользователь в первой строке вводит натуральное число N – количество элементов в массиве. 
# В последующих  строках записаны N целых чисел Ai. Последняя строка содержит число X

numN = int(input("Введите количество элементов в массиве: "))

list_N = []

for i in range(numN):
    list_N.insert(i, int(input("Введите элемент массива: ")))

numX = int(input("Введите число, которое хотите проверить: "))
            
diff = 0
diff_min = abs(numX - list_N[0])
proper_index = 0
for i in range (1,numN):
    if abs(numX - list_N[i]) < diff_min:
        proper_index = i
        diff_min = abs(numX - list_N[i])

print(f"Число {numX} ближе всего по величине к {list_N[proper_index]}")
