n = int(input())
all_a = [int(i) for i in input().split()]

number_taked_place = dict()
taked_places = set()
output = []

for ai in all_a:
    position = number_taked_place.get(ai, 0)

    while position in taked_places:
        position += ai

    number_taked_place[ai] = position
    taked_places.add(position)
    output.append(position)

print(
    " ".join(str(i) for i in output)
)
