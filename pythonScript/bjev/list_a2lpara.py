# coding=utf8
# the above tag defines encoding for this document and is for Python 2.x compatibility

import re
import pandas as pd

regex = r"/begin CHARACTERISTIC\s(\w*)\s\S([\u4e00-\u9fa5\w]+)\S"

# test_str = ("Read the LbSOC_TempMaxErr_flg \n"
# 	"LeSOC_TempMaxRaw_degC=KeSOC_CTMaxLim_degC+1\n"
# 	"Read the LbSOC_TempMaxErr_flg ")

path = 'N60_012012_1019.a2l'

with open(path, 'r') as file:
    test_str = file.read().replace('\n', ' ')

# print(test_str)

# f = open(path, 'rb')

# test_str = f.read()

matches = re.finditer(regex, test_str, re.MULTILINE)

# print(matches)

list = []

for matchNum, match in enumerate(matches, start=1):
    
    # print ("Match {matchNum} was found at {start}-{end}: {match}".format(matchNum = matchNum, start = match.start(), end = match.end(), match = match.group()))
    list.append((match.group(1), match.group(2)))
    # print(match.group())
    # print('\n')
    # print('Got {match}'.format(match = match.group()))


    # for groupNum in range(0, len(match.groups())):
        # groupNum = groupNum + 1
        
        # print ("Group {groupNum} found at {start}-{end}: {group}".format(groupNum = groupNum, start = match.start(groupNum), end = match.end(groupNum), group = match.group(groupNum)))

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

# print(len(list))
# print(len(list2))
    
df = pd.DataFrame(list)
df.columns = ['parameter', 'chinese']

df.to_csv('a2l.csv', index=False)