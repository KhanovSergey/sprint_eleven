def data_count(t, matrix):
    numbers = []
    max_point = 0
    for i in range(1, 10):
        count = matrix.count(str(i))
        numbers.append(count)

    for i, elem in enumerate(numbers):
        if elem == 0:
            continue
        if int(elem) <= t:
            max_point += 1
    print(max_point)


def main():
    t = int(input()) * 2
    matrix = ''
    matrix = ''.join([matrix + input() for i in range(4)])
    data_count(t, matrix)


if __name__ == '__main__':
    main()

# def data_input():
#     k = int(input()) * 2
#     matrix = ''
#     matrix = ''.join([matrix + input() for i in range(4)])
#     return k, matrix
#
#
# def main():
#     k, matrix = data_input()
#     numbers = []
#     scores = 0
#     for i in range(1, 10):
#         count = matrix.count(str(i))
#         numbers.append(count)
#
#     for i, elem in enumerate(numbers):
#         if elem == 0:
#             continue
#         if int(elem) <= k:
#             scores += 1
#     print(scores)
#
#
# if __name__ == '__main__':
#     main()
