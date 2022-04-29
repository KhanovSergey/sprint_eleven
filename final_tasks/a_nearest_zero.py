def main():
    # n = int(input())
    # f = input().split()
    n = 5
    f = [0, 1, 4, 9, 0]
    # count = 0
    f_zer = []
    f_rez = []
    for i in range(n):
        if f[i] == 0:
            f_zer.append(i)
            f_rez.append(0)
        else:
            f_rez.append(1)
    print(f_zer)
    print(f_rez)
    #print(f_zer[1])
    # f_rez = []
    #print(f_zer[-1])
    # for j in range(n):
    #     if f_zer[-1] <= n - 1:


    tot = f_zer[1] - f_zer[0]
    if tot % 2 == 0 and tot <= 4:
        f_rez[2] = 2
        # for j in range(2, n):
        #     f_rez.insert(2, 2)
    print(f_rez)



    #     if len(word) > count:
    #         res_word = word
    #         count = len(word)
    # print(res_word)
    # print(count)


if __name__ == '__main__':
    main()

