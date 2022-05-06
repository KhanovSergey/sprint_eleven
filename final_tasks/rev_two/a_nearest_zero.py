"""
ID 68147761
Code edits after the second review.
"""

import sys


def zero_index(house_num):
    f_zero = [i for i, value in enumerate(house_num) if value == 0]
    return f_zero


def sort_zero(street_len, house_num):
    len_to_zero = []
    safe_street_len = street_len

    f_zero_sort = zero_index(house_num)

    if f_zero_sort[0] == 0:
        len_to_zero.append(0)
    else:
        for i in reversed(range(f_zero_sort[0] + 1)):
            len_to_zero.append(i)

    for j in range(0, len(f_zero_sort) - 1):
        difference = int(f_zero_sort[j + 1]) - int(f_zero_sort[j])
        street_len = int(difference / 2 + 1)
        if (difference + 1) % 2 == 0:
            for i in range(1, street_len):
                len_to_zero.append(i)
            for i in reversed(range(0, street_len)):
                len_to_zero.append(i)
        else:
            for i in range(1, street_len - 1):
                len_to_zero.append(i)
            for i in reversed(range(0, street_len)):
                len_to_zero.append(i)

    right_zero = f_zero_sort[len(f_zero_sort) - 1]

    if right_zero < safe_street_len - 1:
        for i in range(1, safe_street_len - right_zero):
            len_to_zero.append(i)
    return len_to_zero


def valid_street_len(street_len):
    try:
        int(street_len)
    except ValueError:
        print("Надо ввести число от 1 до 1 000 000")
        sys.exit(1)


def valid_house_num(house_num):
    if not house_num.isnumeric():
        print("В строке ввели одно или более значений не int!")
        sys.exit(1)


def serialize_street_len(street_len):
    valid_street_len(street_len)
    street_len = int(street_len)
    return street_len


def serialize_house_num(house_num):
    valid_house_num(str("".join(house_num)))
    house_num = list(map(int, house_num))
    return house_num


def main():
    street_len_int = serialize_street_len(street_len_input)

    house_num = serialize_house_num(house_num_input)

    if street_len_int == len(house_num):
        return " ".join(map(str, sort_zero(street_len_int, house_num)))
    else:
        return (f'Длина улицы {street_len_int} не равна {len(house_num)} '
                f'(сумме застроеных и пустых участков на карте).')


if __name__ == '__main__':
    street_len_input = input()
    house_num_input = input().strip().split()
    print(main())
