from collections import Counter

S = input()
counts = sorted(Counter(S).items(), key=lambda x: (-x[1], x[0]))

for i in counts[:3]:
    print(*i)