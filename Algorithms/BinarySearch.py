def BinarySearch(array, value):
    length = len(array) - 1
    i = 0

    while i <= length:
        mid = int(i + (length - i)/2)

        if value == array[mid]:
            return mid

        elif value >= array[mid]:
            i = mid + 1

        else:
            length = mid - 1

    return "Not Present in Array"


array = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print(BinarySearch(array, 6))
print(BinarySearch(array, 2))
print(BinarySearch(array, 8))
print(BinarySearch(array, 11))
input()