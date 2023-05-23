N = int(input())

coordinates = list(map(int, input().split()))

distinct_coordinates = sorted(set(coordinates))

compressed_coordinates = {}

for i, coord in enumerate(distinct_coordinates):
    compressed_coordinates[coord] = i

compressed = [compressed_coordinates[coord] for coord in coordinates]

print(' '.join(str(coord) for coord in compressed))
