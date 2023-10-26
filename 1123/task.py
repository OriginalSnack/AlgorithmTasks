n = int(input())
all_a = [int(i) for i in input().split()]

taked_places = set()
output = []

for ai in all_a:
    position = 0

    while position in taked_places:
        position += ai

    taked_places.add(position)
    output.append(position)

print(" ".join(str(i) for i in output))
