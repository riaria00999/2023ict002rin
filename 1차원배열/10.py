N = int(input())
grades = list(map(int, input().split()))
M = max(grades)

new_grades = [(score / M) * 100 for score in grades]
new_average = sum(new_grades) / N

print(new_average)
