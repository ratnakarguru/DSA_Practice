#Hashing In Python
#Prestoring values into some datastructure like list/dict/sets and fetching it 
m = [5,3,4,2,10,8,9]
n = [1,2,3,4,5,6,7]


# for i in m:
#     count = 0
#     for j in n:
#         if j == i:
#             count += 1
#     print(count)
# # print(count)

hash_list = [0] * 11
for num in m:
    hash_list[num] += 1

for num in n:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])