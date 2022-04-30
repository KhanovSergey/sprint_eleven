street_len = 9
house_num = [1, 7, 0, 5, 3, 0, 3, 0, 3]


def sort_zero(street_len, house_num):
    f_zero = []
    for i in range(street_len):
        if house_num[i] == 0:
            f_zero.append(i)
    len_to_zero = []
    i = 0
    m = street_len
    if f_zero[0] != 0:
        for i in reversed(range(f_zero[0] + 1)):
            len_to_zero.append(i)

    for j in range(0, len(f_zero) - 1):
        raz = int(f_zero[j + 1]) - int(f_zero[j])
        if (raz + 1) % 2 == 0:
            street_len = int(raz / 2 + 1)
            for i in range(1, street_len):
                len_to_zero.append(i)
            for i in reversed(range(0, street_len)):
                len_to_zero.append(i)
        else:
            street_len = int(raz / 2 + 1)
            for i in range(1, street_len - 1):
                len_to_zero.append(i)
            for i in reversed(range(0, street_len)):
                len_to_zero.append(i)

    x = f_zero[len(f_zero) - 1]

    if x < m - 1:
        for i in range(1, m - x):
            len_to_zero.append(i)
    return len_to_zero


print(" ".join(map(str, sort_zero(street_len, house_num))))
