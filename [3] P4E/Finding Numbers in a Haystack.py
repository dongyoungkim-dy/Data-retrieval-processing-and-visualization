import re
numlist=list()
flattened=[]
ints=[]
name = input('Enter file:')
if len(name)<1: name='regex_sum_213801.txt'
handle = open(name)
for line in handle:
    num=re.findall('[0-9]+', line)
    if len(num)<1:
        continue
    numlist.append(num)
for sublist in numlist:
    for val in sublist:
        flattened.append(val)
for strings in flattened:
    intss = int(strings)
    ints.append(intss)
print(sum(ints))
