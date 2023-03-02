l = []
for i in range(int(input())):
    nm, sc = input(), float(input())
    l.append([sc, nm])
if not l:
    exit()
l = sorted(l)
minsc = l[0][0]
l = list(filter(lambda x: x[0] != minsc, l))
for s in l:
    if s[0] == l[0][0]:
        print(s[1])