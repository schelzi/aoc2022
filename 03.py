with open('Z:\\python\\adventofcode2022\\03a.txt','r') as f:
    data = [x.strip() for x in f]

# dsplit = [len(x[0])/2 for x in data]
dsplit = [[x[:len(x)//2],x[len(x)//2:]] for x in data]
# dsplit = [[x[:12],x[12:]] for x in data]

sum = 0
# part1
# for item in dsplit:
#     for letter in item[0]:
#         if letter in item[1]:
#             print(letter)
#             if letter.islower():
#                 print(ord(letter)-96)
#                 sum+=ord(letter)-96
#             else:
#                 print(ord(letter)-38)
#                 sum+=ord(letter)-38
#             break
i = 0

while i < len(data):
    for letter in data[i]:
        if letter in data[i+1] and letter in data[i+2]:
            print(letter)
            if letter.islower():
                print(ord(letter)-96)
                sum+=ord(letter)-96
            else:
                print(ord(letter)-38)
                sum+=ord(letter)-38
            i+=3
            break
print(sum)