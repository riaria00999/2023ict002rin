numbers = []
for _ in range(9):
    numbers.append(int(input()))

maximum = max(numbers)
index = numbers.index(maximum)

print(maximum)
print(index + 1)
