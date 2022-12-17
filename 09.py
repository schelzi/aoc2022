import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

cols = {0:'purple',1:'green',2:'blue',3:'red',4:'yellow',5:'brown',6:'black',7:'pink',8:'orange',9:'turquoise'}

def getData():
    moveset = []
    with open('09a.txt','r') as f:
        data = [x.strip().split() for x in f]


    for i in data:
        i[1] = int(i[1])
        moveset.append(np.array([0,0]))
        if i[0] == 'L':
            for _ in range(i[1]):
                moveset.append(np.array([-1,0]))
        elif i[0] == 'R':
            for _ in range(i[1]):
                moveset.append(np.array([1,0]))
        elif i[0] == 'U':
            for _ in range(i[1]):
                moveset.append(np.array([0,1]))
        else:
            for _ in range(i[1]):
                moveset.append(np.array([0,-1]))
    return moveset
def length(vector):
    return (vector[0] ** 2 + vector[1] ** 2) ** 0.5
# def animate(i):
#     ax.clear()
#     hpoint = all_points[i][0]
#     tpoint = all_points[i][1]
#     for j in range(len(all_points[i])):
#         col = cols[j]
#         ax.plot(all_points[i][j][0], all_points[i][j][1], color=col, label='original', marker='o')
   
#     ax.set_xlim([0,6])
#     ax.set_ylim([0,6])

# fig, ax = plt.subplots(1,1)
# fig.set_size_inches(5,5)

# part 1
# rope = [np.zeros(2), np.zeros(2)]

rope = [np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2), np.zeros(2)]
tail_positions = [[0.0, 0.0]]
all_points = []

moveset = getData()
# print(moveset,start,head,tail)
for i, step in enumerate(moveset):
    # if i < 20:
    # debug before full move instruction
    if not step.any() :
        print(rope)
    all_points.append([tuple(x) for x in rope])
    move = np.zeros(2)
    # plt.plot(head)
    # plt.plot(tail)
    # plt.show()
    # debug
    # if i >= 19:
    #     print()
    ht = np.copy(rope)
    rope[0] += step
    for j in range(1,len(rope)):
        # tt = tail.copy()
        l = length(rope[j] - rope[j-1])
        if l == 2:
            rope[j] += (rope[j-1] - rope[j]) / 2
            move = np.zeros(2)
        elif l < 2:
            # print(head,tail)
            break
        elif l > 2:
            if any(move):
                rope[j] += move
            else:
                move = ht[j-1] - rope[j]
                rope[j] = np.copy(ht[j-1])
                
    if list(rope[len(rope)-1]) not in tail_positions:
        tail_positions.append(list(rope[len(rope)-1]))
    # print(head,tail)

# ani = FuncAnimation(fig, animate, frames=len(all_points), interval= 50, repeat = False)
# plt.show()

print(len(tail_positions))
#2374 too high