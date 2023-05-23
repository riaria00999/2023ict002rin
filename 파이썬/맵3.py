n = int(input())

currently_in_company = set()

for _ in range(n):
    name, action = input().split()
    if action == "enter":
        currently_in_company.add(name)
    else:
        currently_in_company.remove(name)

names_sorted = sorted(currently_in_company, reverse=True)

for name in names_sorted:
    print(name)
