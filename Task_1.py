n = int(input())
l = []
for i in range(n):
    l.append((lambda x: 1 if i % 2 == 0 else 0)(i))
print(l)