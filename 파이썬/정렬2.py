numbers = []
for i in range(5):
    number = int(input())
    numbers.append(number)

average = sum(numbers) // 5

sorted_numbers = sorted(numbers)
median = sorted_numbers[2]

print(average)
print(median)
