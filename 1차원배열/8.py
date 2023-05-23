numbers = []
for i in range(10):
    number = int(input())
    numbers.append(number)

remainders = set()
for number in numbers:
    remainder = number % 42
    remainders.add(remainder)

print(len(remainders))
