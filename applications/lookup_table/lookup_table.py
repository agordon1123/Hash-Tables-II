import math
import random

hash_pow = {}
hash_fact = {0: 1}

for i in range(2, 15):
    for y in range(3, 7):
        if (i, y) not in hash_pow:
            num_pow = int(math.pow(i, y))
            hash_pow[(i, y)] = num_pow

def fact(num):
    if num not in hash_fact:
        hash_fact[num] = math.factorial(num)
    return hash_fact[num]

def slowfun(x, y):
    print(x, ', ', y)
    # TODO: Modify to produce the same results, but much faster
    # v = math.pow(x, y)
    # OLD = ^ , NEW = v
    v = hash_pow[(x, y)]
    # v = math.factorial(v)
    # OLD = ^ , NEW = v
    v = fact(v)
    v //= (x + y)
    v %= 982451653

    return v


# Do not modify below this line!

for i in range(50000):
    x = random.randrange(2, 14)
    y = random.randrange(3, 6)
    print(f'{i}: {x},{y}: {slowfun(x, y)}')
