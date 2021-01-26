# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import pandas as pd

regex = r"ID-BMS-\d{3}|(\w*)_(\w*)_(\w*)"

# test_str = ("Read the LbSOC_TempMaxErr_flg \n"
# 	"LeSOC_TempMaxRaw_degC=KeSOC_CTMaxLim_degC+1\n"
# 	"Read the LbSOC_TempMaxErr_flg ")

path = 'BMS_TestCase_1129.txt'

with open(path, 'r', encoding='UTF-8') as file:
    test_str = file.read().replace('\n', ' ')


# f = open(path, 'rb')

# test_str = f.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

# print(matches)

list = []
list2 = []

for matchNum, match in enumerate(matches, start=1):
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    list.append(match.group())
    # print(match.group())
    # print('\n')
    # print('Got {match}'.format(match = match.group()))


    # for groupNum in range(0, len(match.groups())):
    #     groupNum = groupNum + 1
        
    #     print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

# Note: for Python 2.7 compatibility, use ur"" to prefix the regex and u"" to prefix the test string and substitution.

# print(list)

#     if fnmatch(match.group, 'FT-BMS-\d*':
#          list.append((match.group, match.group(matchNum + 1)))

# for elem,next_elem in zip(list, list[1:]+[list[0]]):
#     if fnmatch(elem, 'FT-BMS-\d*'): 
#         # list.append((i,match+1))
#         print('{first}, {second}'.format(first = elem, second = next_elem))
#         i++
#         dfid = match[i]

#     list.append((dfid, match))
# print(list)
for idx in range(0, len(list)):
    # print(list[idx])
    # if re.search('FT-BMS-\d*', list[idx-1]):
    #     continue
    if re.search('ID-BMS-\d*', list[idx]):
        # print('match succeed')
        # print(elem)
        numid = list[idx]
        para = list[(idx + 1) % len(list)]
        list2.append((numid, para))
    else:
        list2.append((numid, list[idx]))

# print(list2)

# print(len(list))
# print(len(list2))
    
df = pd.DataFrame(list2)
df.columns = ['id', 'parameter']
# print(df)

df.to_csv('Insulation detection.csv', index=False)