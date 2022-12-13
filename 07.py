with open('07a.txt','r') as f:
    data = [x.strip() for x in f]

fs = {'/':'dir'}
cwd = ''

for line in data:
    if line[0] == '$':
        if '$ ls' in line:
            continue
        
        
        if '$ cd 'in line:
            if line.split()[2] == '..':
                cwd = '/'.join(cwd.split('/')[:-1])
            else:
                cwd = cwd + '/'+ line.split()[2]
    elif line[0] == 'd':
        fs[cwd + '/'+ line.split()[1]] = 'dir'
    else:
        fs[cwd + '/'+ line.split()[1]] = line.split()[0]

# print(fs)

dirs = {dir: 0 for dir in fs if fs[dir] == 'dir' }
files = {file: size for file,size in fs.items() if size.isnumeric() }

for file in files:
    if file.count('/') > 1:
        parentdir = file[:file.rfind('/')]
    else:
        parentdir = '/'
    dirs[parentdir] += int(files[file])

total = (sum([dirs[dir] for dir in dirs]))

for item in sorted(dirs, key =  lambda x: x.count('/'),reverse=True):
    if item.count('/') > 1:
        parentdir = item[:item.rfind('/')]
    else:
        parentdir = '/'
    dirs[parentdir] += dirs[item]

sum = 0

for dir in dirs:
    if dirs[dir] < 100000:
        sum += dirs[dir]

print('Sum of dirs <100k = '+str(sum))

free = 70000000 - total
needed = 30000000 - free

print('Smallest dir to delete to make needed space of '+str(needed)+': '+str(min([dirs[dir] for dir in dirs if dirs[dir] >= needed])))

# sbs = sorted(dirs, key = lambda x: dirs[x])
# print(sbs)
# for item in sbs:

    # print(item,dirs[item])
# print(needed)
