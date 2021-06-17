def selctionSort(list):
    for i in range(len(list)):
        current_minimum = i
        for j in range(i + 1, len(list)):
            if list[current_minimum] > list[j]:
                current_minimum = j
        list[i], list[current_minimum] = list[current_minimum], list[i]


A = [64, 25, 12, 22, 11]
selctionSort(A)
print(A)
