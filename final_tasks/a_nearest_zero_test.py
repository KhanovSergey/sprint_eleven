def in_full(z_l, z_r, fun):
    if z_l is None:
        for i in range(z_r):
            fun.append(1)
            i += 1
        fun.append(0)

    # for z_l in range(z_r):
    #     if fun.append(1)
    #     i += 1
    #     fun.append(0)
    # return fun


def main():
    # n = int(input())
    # f = input().split()
    # n = 12
    # f = [4, 5, 7, 0, 1, 4, 9, 0, 2, 3, 5, 0]
    n = 6
    f = [0, 7, 9, 4, 8, 20]
    # count = 0
    f_zer = []
    f_rez = []
    f_rez_one = []
    for i in range(n):
        if f[i] == 0:
            f_zer.append(i)
            f_rez_one.append(0)
        else:
            f_rez_one.append(1)
    print(f_zer)
    print(f_rez_one)
    fun = []
    # print(in_full(None, f_zer[0], fun))
    # print(len(f_zer))
    if len(f_zer) > 1:
        i = 0
        for i in range(len(f_zer)-1):
            raz = int(f_zer[i + 1] - f_zer[i])
            if (raz + 1) % 2 != 0:
                f_ind = raz / 2 + f_zer[i]
                f_rez_one[int(f_ind)] = 2
            # i += 1
        print(f_rez_one)


        # for i in range(len(f_zer)):
        #     raz = f_zer[i + 1] - f_zer[i]
        #     if raz % 2 != 0:
        #         f_ind = raz / 2 + f_zer[i]
        #         f_rez_one[f_ind] = 2
        #     i = f_zer[i + 1]

        # i = 0
        # while i < len(f_zer):
        #     raz = f_zer[i + 1] - f_zer[i]
        #     if raz % 2 != 0:
        #         f_ind = raz / 2 + f_zer[i]
        #         f_rez_one[f_ind] = 2
        #     i = f_zer[i + 1]
        # print(f_rez_one)


# print(f_rez)
# print(f_zer[1])
# f_rez = []
# print(f_zer[-1])
# for j in range(n):
#     if f_zer[-1] <= n - 1:

#
# tot = f_zer[1] - f_zer[0]
# if tot % 2 == 0 and tot <= 4:
#     f_rez[2] = 2
#     # for j in range(2, n):
#     #     f_rez.insert(2, 2)
# print(f_rez)

#     if len(word) > count:
#         res_word = word
#         count = len(word)
# print(res_word)
# print(count)


if __name__ == '__main__':
    main()
