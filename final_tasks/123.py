# n = 13
ff = [4, 5, 7, 0, 1, 4, 9, 0, 2, 3, 5, 2, 0]
print(ff)

f_zero = [3, 7, 12]
f = []
for i in reversed(range(f_zero[0] + 1)):
    f.append(i)

for i in range(1, 3):
    f.append(i)

for i in reversed(range(0, 2)):
    f.append(i)

for i in range(1, 4):
    f.append(i)

for i in reversed(range(0, 3)):
    f.append(i)

print(f)
print(" ".join(map(str, f)))
