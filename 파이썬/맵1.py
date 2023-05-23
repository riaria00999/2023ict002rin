N = int(input())

number_cards = set(map(int, input().split()))

M = int(input())

numbers_to_check = list(map(int, input().split()))

results = []
for number in numbers_to_check:
    if number in number_cards:
        results.append('1')
    else:
        results.append('0')

print(' '.join(results))
