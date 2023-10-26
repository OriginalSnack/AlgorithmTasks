s = input()
is_everything_Ok = True
x, y = 0, 0
lst = {(x, y)}
for item in s:
    if item == "N":
        x, y = x, y + 1
    elif item == "S":
        x, y = x, y - 1
    elif item == "W":
        x, y = x + 1, y
    elif item == "E":
        x, y = x - 1, y
    t = (x, y)
    if t in lst:
        print("Something goes wrong...")
        is_everything_Ok = False
        break
    lst.add((x, y))
if is_everything_Ok:
    print("Looks OK.")