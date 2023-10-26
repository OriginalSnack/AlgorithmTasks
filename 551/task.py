from math import ceil, floor, log

l, r = [int(i) for i in input().split()]

n = 2
max_n = 1

while n < 1200:
    # знайшли основу яку треба піднести в n щоб було l/r
    l2 = log(l, n)
    r2 = log(r, n)

    do_we_have_any_integers = any(i for i in range(floor(l2), ceil(r2) + 1) if l <= i ** n <= r)
    if do_we_have_any_integers:
        max_n = n

    n += 1

print(max_n)
