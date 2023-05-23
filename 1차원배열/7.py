submitted = set()
for _ in range(28):
    n = int(input())
    submitted.add(n)
missing = []
for i in range(1, 31):
    if i not in submitted:
        missing.append(i)
        if len(missing) == 2:
            break
print(min(missing))
print(max(missing))
