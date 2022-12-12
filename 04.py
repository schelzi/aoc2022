with open('Z:\\python\\adventofcode2022\\04a.txt','r') as f:
    data = [x.strip().split(',') for x in f]

# print(data)
ds = [[d[0].split('-'),d[1].split('-')] for d in data]
# print(ds)

count = 0

# part 1
# for item in ds:
#     if int(item[0][0]) >= int(item[1][0]) and int(item[0][1]) <= int(item[1][1]):
#         count+=1
#     elif int(item[1][0]) >= int(item[0][0]) and int(item[1][1]) <= int(item[0][1]):
#         count+=1

for item in ds:
    if int(item[0][1]) >= int(item[1][0]) and int(item[0][1]) <= int(item[1][1]):
        count+=1
    elif int(item[1][1]) >= int(item[0][0]) and int(item[1][1]) <= int(item[0][1]):
        count+=1

print(count)