def max_3_multiplication(array):
    if len(array) > 0:
        max1 = max(array[0:3])
        array.remove(max1)
        max2, max3 = max(array[0:2]), min(array[0:2])
        min1, min2 = min(array[0:2]), max(array[0:2])
        for i in range(2, len(array)):
            if array[i] >= max1:
                max3, max2, max1 = max2, max1, array[i]
            elif array[i] >= max2:
                max3, max2 = max2, array[i]
            elif array[i] >= max3:
                max3 = array[i]
            if min1 >= array[i]:
                min1, min2 = array[i], min1
            elif min2 >= array[i]:
                min2 = array[i]
        if max1 * max2 * max3 > max1 * min2 * min1:
            print(max3, max2, max1)
        else:
            print(min2, min1, max1)
    else:
        print(0)


with open("19.1.txt", "r") as file:
    array = list(map(int, file.read().strip().split()))


max_3_multiplication(array)