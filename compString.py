from itertools import groupby 
data = input()

print(*[(len(list(y)), int(x)) for x,y in groupby(data)])