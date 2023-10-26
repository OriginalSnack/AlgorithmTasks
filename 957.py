n = int(input())
words = [input() for i in range(n)]


# # first approach Pythonic
# words = ["".join(sorted(list(word))) for word in words]
# print(len(set(words)))
def f(s):
    lst = [0] * (ord("z") - ord("a") + 1)
    for letter in s:
        index = ord(letter) - ord("a")
        lst[index] += 1
    return tuple(lst)


words = [f(i) for i in words]

print(len(set(words)))
