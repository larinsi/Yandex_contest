import random

def style(n, tshirts, m, pants):
    i = j = 0
    best_tshirt = tshirts[i]
    best_pants = pants[j]
    best_diff = abs(best_tshirt - best_pants)
    for k in range(n + m):

    return best_tshirt, best_pants, best_diff


def style_naiv(n, tshirts, m, pants):
    best_tshirt = tshirts[0]
    best_pants = pants[0]
    best_diff = abs(best_tshirt - best_pants)
    for i in range(n):
        for j in range(m):
            if best_diff > abs(tshirts[i] - pants[j]):
                best_diff = abs(tshirts[i] - pants[j])
                best_tshirt = tshirts[i]
                best_pants = pants[j]
    return best_tshirt, best_pants, best_diff


def test_functions():
    max_size_of_array = 20
    max_size_of_color = 50
    n = random.randint(1, max_size_of_array)
    m = random.randint(1, max_size_of_array)
    tshirts_set = set([random.randint(1, max_size_of_color) for _ in range(n)])
    pants_set = set([random.randint(1, max_size_of_color) for _ in range(m)])
    tshirts = sorted(list(tshirts_set))
    pants = sorted(pants_set)
    n = len(tshirts)
    m = len(pants)
    print(*style(n, tshirts, m, pants))
    print(*style_naiv(n, tshirts, m, pants))
    print(n, tshirts)
    print(m, pants)


test_functions()

# tshirts = 2, 9, 11, 12, 15, 16, 17, 18
# pants = 3, 5, 9, 10, 13, 14, 15, 16, 20
#
# print(*style(8, tshirts, 9, pants))
# print(*style_naiv(8, tshirts, 9, pants))



# with open("41.1.txt", "r") as file:
#     n = int(file.readline().strip())
#     tshirts = list(map(int, file.readline().strip().split()))
#     m = int(file.readline().strip())
#     pants = list(map(int, file.readline().strip().split()))
#
# print(*style(n, tshirts, m, pants))
