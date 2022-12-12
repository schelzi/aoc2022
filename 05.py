# l1 = ['N','S','D','C','V','Q','T']
# l2 = ['M','F','V']
# l3 = ['F','Q','W','D','P','N','H','M']
dic = {'1':'NSDCVQT','2':'MFV','3':'FQWDPNHM','4':'DQRTF','5':'RFMNQHVB','6':'CFGNPWQ','7':'WFRLCT','8':'TZNS','9':'MSDJRQHN'}

with open('Z:\\python\\adventofcode2022\\05a.txt','r') as f:
    data = [x.strip().split() for x in f]
# remove all words from move instruction lists
for dat in data:
    for word in dat:
        if not word.isnumeric():
            dat.remove(word)
#lists of instructions -> format: count, from, to

# part 1
# for instructionset in data:
#     for count in range(int(instructionset[0])):
#         letter = dic[instructionset[1]][-1]
#         dic[instructionset[2]]=dic[instructionset[2]]+letter
#         dic[instructionset[1]]=dic[instructionset[1]][:-1]

for instructionset in data:
    num = int(instructionset[0])
    letters = dic[instructionset[1]][-num:]
    dic[instructionset[2]]=dic[instructionset[2]]+letters
    dic[instructionset[1]]=dic[instructionset[1]][:-num]


res = ''
for i in range(1,10):
    res += dic[str(i)][-1]

print(res)