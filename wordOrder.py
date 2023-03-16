from collections import Counter
n = int(input())
c = Counter([input() for _ in range(n)])
print(len(c))
print(' '.join(map(str,c.values())))