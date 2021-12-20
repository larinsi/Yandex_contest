def sum_of_nums(n: int, k: int, array: list) -> int:
    result = left = 0
    prefix_sum = [0] * (n + 1)
    for i in range(1, n+1):
        prefix_sum[i] = prefix_sum[i-1] + array[i-1]
    for right in range(len(prefix_sum)):
        if prefix_sum[right] - prefix_sum[left] == k:
            result += 1
            left += 1
        if right == len(prefix_sum) - 1:
            while left < len(prefix_sum) - 1:
                if prefix_sum[right] - prefix_sum[left] == k:
                    result += 1
                left += 1
    return result


with open("Tests/42.1.txt", "r") as file:
    n, k = map(int, file.readline().strip().split())
    array = list(map(int, file.readline().strip().split()))

print(sum_of_nums(n=n, k=k, array=array))

