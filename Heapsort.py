def heapify(arr, n, i):
    largest = i
    left = 2 * i + 1  # Левый элемент
    right = 2 * i + 2  # Правый элемент

    # Если левый элемент больше корня
    if left < n and arr[left] > arr[largest]:
        largest = left

    # Если правый элемент больше, чем наибольший элемент на данный момент
    if right < n and arr[right] > arr[largest]:
        largest = right

    # Если наибольший элемент не корень
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]  # Меняем местами

        heapify(arr, n, largest)

def heapsort(arr):
    n = len(arr)

    # Построение кучи
    for i in range(n // 2 - 1, -1, -1):
        heapify(arr, n, i)

    # Один за другим извлекаем элементы из кучи
    for i in range(n - 1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]  # Меняем местами
        heapify(arr, i, 0)


arr = [12, 11, 13, 5, 6, 7,1,6]
heapsort(arr)
print("Отсортированный массив:", arr)