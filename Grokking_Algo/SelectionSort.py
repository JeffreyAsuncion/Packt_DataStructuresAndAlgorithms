def findSmallest(arr):
    smallest = arr[0]
    smallest_index = 0
    print(len(arr))
    for i in range(1, len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
            smallest_index = i
    return smallest_index

def selectionSort(arr):
    newArr = []
    for i in range(len(arr)):
        smallest = findSmallest(arr)
        # print(len(arr))
        newArr.append(arr.pop(smallest))
        # print(len(arr))
    return newArr

print(selectionSort([5, 3, 6, 2, 10]))