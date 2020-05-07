"""
find all a, b, c, d in q such that
f(a) + f(b) = f(c) - f(d)
"""

# q = set(range(1, 10))
# q = set(range(1, 200))
q = (1, 3, 4, 7, 12)


def f(x):
    return x * 4 + 6

# TODO: Implement me.

d_add = {}
d_sub = {}

for i in q:
    for j in q:
        val = f(i) + f(j)
        if val not in d_add:
            d_add[val] = set()
        d_add[val].add((i, j))
        if i != j:
            d_add[val].add((j, i))

for i in q:
    for j in q:
        val = f(j) - f(i)
        if val in d_add:
            for comb in d_add[val]:
                print(f'f({comb[0]}) + f({comb[1]}) = f({j}) - f({i})')
