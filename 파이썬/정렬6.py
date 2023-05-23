# Read the number
N = input()

digits = list(N)

digits.sort(reverse=True)

sorted_number = ''.join(digits)

print(sorted_number)
