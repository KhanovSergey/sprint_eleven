n = 16
m = 16
f = [7, 0, 5, 66, 4, 5, 0, 3, 4, 3, 0, 3, 4, 5, 0, 3]
# print(ff)

f_zero = []
for i in range(n):
    if f[i] == 0:
        f_zero.append(i)
print(f)
print(f_zero)
f = []
i = 0
# l = f_zero[len(f_zero)]
if f_zero[0] != 0:
    for i in reversed(range(f_zero[0] + 1)):
        f.append(i)

# print(len(f_zero))
for j in range(0, len(f_zero) - 1):
    raz = int(f_zero[j + 1]) - int(f_zero[j])
    if (raz + 1) % 2 == 0:
        print(f' чет {int(raz / 2)}')
        # n = int(f_zero[j] + raz / 2)
        n = int(raz / 2 + 1)
        for i in range(1, n):
            f.append(i)
        for i in reversed(range(0, n)):
            f.append(i)
    else:
        print(f' нечет {int(raz / 2)}')
        # n = int(f_zero[j]) + int(raz / 2)
        n = int(raz / 2 + 1)
        print(f' нечет - нечет {n}')
        for i in range(1, n - 1):
            f.append(i)
        for i in reversed(range(0, n)):
            f.append(i)
print(len(f))
# print(f)
x = f_zero[len(f_zero) - 1]
print(x)
print(n)
if x < m-1:
    for i in range(1, m - x):
        print(f'iiiiiiiiiiiiiiii {i}')
        f.append(i)

#
#
# for i in range(1, 4):
#     f.append(i)
#
# for i in reversed(range(0, 3)):
#     f.append(i)


print(" ".join(map(str, f)))
