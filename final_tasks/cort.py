from operator import itemgetter

f_zero = []
len_to_zero = []
street_len = 5
house_num = [0, 1, 4, 9, 0]

for i in range(street_len):
    if house_num[i] == 0:
        f_zero.append(i)

print(f_zero)
# res = sorted(house_num, key=itemgetter(0))
res = sorted(int(house_num[0]))
print(f'sort_list   {res}')
