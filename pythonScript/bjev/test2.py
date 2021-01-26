import re

list = ['ABC', 'ABC', '123', 'ABD', '123']
list2 = []

# for idx, elem in enumerate(list):
#     # print(elem)
#     if re.search('AB\w*', elem):
#         print('match succeed')
#         # print(elem)
#         alp = elem
#         num = list[(idx + 1) % len(list)]
#         list2.append((alp, num))
#         continue
#     list2.append((alp, elem))

# print(list2)
    
# print('abc = {a}, 123 = {b}'.format(a = elem, b = nextelem))

# for idx, elem in enumerate(list):
#     if re.search('AB\w', elem):
#         continue
#     print(idx, elem)

for idx in range(0, len(list)):
    # print(list[idx])
    if re.search('AB.*', list[idx-1]):.
        continue
    if re.search('AB.*', list[idx]):
        print('match succeed')
        # print(elem)
        alp = list[idx]
        num = list[(idx + 1) % len(list)]
        list2.append((alp, num))
    else:
        list2.append((alp, list[idx]))

print(list2)
