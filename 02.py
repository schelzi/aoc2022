with open('Z:\\python\\adventofcode2022\\02a.txt','r') as f:
    data = [x.split() for x in f]

print(data)
sum = 0
win = {'A':2,'B':3,'C':1}
loss = {'A':3,'B':1,'C':2} 
for d in data:

#   part 1
#     res = ord(d[1])-ord(d[0])
#     if res == 22 or res == 25:
#         score = 0
#     elif res == 23:
#         score = 3
#     else:
#         score = 6
#     print(ord(d[1]))
#     base = abs(ord(d[1])-87)
#     print(base, score)
#     sum+=base+score
# print(sum)




    if ord(d[1]) == 88:
        score = 0
        base = loss[d[0]]
    elif ord(d[1]) == 89:
        score = 3
        base = abs(64-ord(d[0]))
    else:
        score = 6
        base = win[d[0]]
    sum+=base+score
    print(base,score)
print(sum)