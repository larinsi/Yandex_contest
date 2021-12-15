# начинаем с середины
def symmetric_sequence(n, array):
    max_sym_len = 0
    for k in range(n):
        slice = array[k:]
        if slice == slice[::-1]:
            max_sym_len = len(slice)
            break
    print(n - max_sym_len)
    if n != max_sym_len:
        result = array[:-max_sym_len][::-1]
        print(" ".join(str(elem) for elem in result))


with open("Tests/16.3.txt", 'r') as file:
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))

symmetric_sequence(n, array)
