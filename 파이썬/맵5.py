N = int(input())

number_cards = list(map(int, input().split()))

M = int(input())
numbers_to_find = list(map(int, input().split()))

count = {}

for num in number_cards:
    count[num] = count.get(num, 0) + 1

for num in numbers_to_find:
    print(count.get(num, 0), end=' ')
