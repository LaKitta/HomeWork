# read file, collections: dict, tuple, list

fhan = open('mbox-short.txt')

nameList = []

for line in fhan:
    if line.startswith('From'):
        nameList.append(line.split()[1])

# print(nameList)

histgram = dict()

for name in nameList:
    histgram[name] = histgram.get(name, 0) + 1

# print(histgram)

"""
max = -1
maxWord = ''

for word, count in histgram.items():
    if count > max:
        max = count
        maxWord = word

print(maxWord, max)
"""
"""
sortedList = list()
for k,v in histgram.items():
    sortedList.append((v,k))

print(sorted(sortedList, reverse=True)[:3])
"""

print(sorted([(v,k) for k,v in histgram.items()], reverse=True)[:3])


