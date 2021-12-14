import random

def style(n, tshirts, m, pants):
    best_tshirt = tshirts[0]
    best_pants = pants[0]
    best_diff = abs(best_tshirt - best_pants)
    j = 0
    for i in range(n):
        while j < m - 1:
            if best_diff == 0:
                return best_tshirt, best_pants
            j += 1
            if best_diff >= abs(tshirts[i] - pants[j]):
                best_diff = abs(tshirts[i] - pants[j])
                best_tshirt = tshirts[i]
                best_pants = pants[j]
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
    n = random.randint(1, 50)
    m = random.randint(1, 50)
    tshirts = sorted([random.randint(1, 100000) for _ in range(n)])
    pants = sorted([random.randint(1, 100000) for _ in range(m)])
    print(*style(n, tshirts, m, pants))
    print(*style_naiv(n, tshirts, m, pants))
    # print(n, tshirts)
    # print(m, pants)


test_functions()




#with open("41.3.txt", "r") as file:
 #   n = int(file.readline().strip())
  #  tshirts = list(map(int, file.readline().strip().split()))
   # m = int(file.readline().strip())
    #pants = list(map(int, file.readline().strip().split()))

#print(*style(n, tshirts, m, pants))
