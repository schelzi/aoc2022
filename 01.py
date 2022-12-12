with open('Z:\\python\\adventofcode2022\\01a.txt', 'r') as f:
    data = [x.strip() for x in f]
print(data)
sums = []
sum = 0
for cal in data:
    if cal != '':
        sum += int(cal)
    else:
        sums.append(sum)
        sum = 0

sums2 = max(sums)
print(max(sums))
sums.remove(max(sums))
sums2 += max(sums)
print(max(sums))
sums.remove(max(sums))
sums2 += max(sums)
print(max(sums))
sums.remove(max(sums))
print(sums2)