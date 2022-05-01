def sort_zero(street_len, house_num):
    f_zero = []
    len_to_zero = []
    m = street_len

    for i in range(street_len):
        if house_num[i] == 0:
            f_zero.append(i)

    if f_zero[0] == 0:
        len_to_zero.append(0)
    else:
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


def main():
    street_len = int(input())
    house_num = list(map(int, input().strip().split()))
    print(" ".join(map(str, sort_zero(street_len, house_num))))


if __name__ == '__main__':
    main()
