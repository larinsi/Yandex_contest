# начинаем с середины
def symmetric_sequence(n, array):
    pass



with open("Tests/16.1.txt", 'r') as file:
    n = int(file.readline().strip())
    array = list(map(int, file.readline().strip().split()))

symmetric_sequence(n, array)