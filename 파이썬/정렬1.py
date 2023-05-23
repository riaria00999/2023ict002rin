N = int(input())

numbers = []
for i in range(N):
    number = int(input())
    numbers.append(number)

sorted_numbers = sorted(numbers)

for number in sorted_numbers:
    print(number)
