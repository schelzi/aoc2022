with open('08a.txt','r') as f:
    data = [x.strip() for x in f]

vis = len(data[0]) + len(data[-1]) + 2*len(data)-4 

scores = []
for i in range(1,len(data)-1):
    for j in range(1,len(data[i])-1):
        score=[]
        tree = data[i][j]
        l = [data[i][tr] for tr in range(0,j)]
        r = [data[i][tr] for tr in range(j+1,len(data[i]))]
        u = [data[tr][j] for tr in range(0,i)]
        d = [data[tr][j] for tr in range(i+1,len(data))]
        if any([tree > max(u), tree > max(d), tree > max(l), tree > max(r)]):
            vis+=1
            # print(tree, '>', max(u),max(d),max(l),max(r))

            l = reversed(l)
            u = reversed(u)
        
            for dir in ['l','r','u','d']:
                count = 0
                for item in eval(dir):
                    if item < tree:
                        count+=1
                    else:
                        count+=1
                        
                        break
                score.append(count)
            from functools import reduce
            scores.append(reduce((lambda x,y: x*y),score))


print('visible trees:', vis)
print('max scenery score:', max(scores))