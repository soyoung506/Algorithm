test_cases = int(input())
nums = [int(input()) for _ in range(test_cases)]

cache = [1] + [0] * 11


def find(num):
    if not cache[num]:
        cache[num] = sum(map(lambda x: find(x), range(max(num - 3, 0), num)))
    return cache[num]


for num in nums:
    print(find(num))