class Cpu:
    def __init__(self):
        self.signal = 1
        self.clock = 0
        self.values = []
        self.targets = [20,60,100,140,180,220]
        self.rendered=['']
        self.row = 0
        
        pass
    def add_clock(self, count = 1):
        self.clock+=count
        self.check_target_values()
        self.render(self.row)
    
    def check_target_values(self):
        if self.clock in self.targets:
            self.values.append(self.signal*self.clock)

    def calc(self, instruction):
        if instruction == 'noop':
            self.add_clock()
            

        else:
            for _ in range(2):
                self.add_clock()
            self.signal += int(instruction.split()[1])

    def render(self,row):
        
        if abs(self.clock % 40 -1 - self.signal) <= 1:
            self.rendered[row] += '#'
        else:
            self.rendered[row] += '.'
        if self.clock % 40 == 0:
            self.rendered.append('')
            self.row = self.clock // 40



    
with open('10a.txt','r') as f:
    data = [x.strip() for x in f]
a = Cpu()
for i in data:
    a.calc(i)

print('part1:')
print(sum(a.values))
print('\npart2:')

for i in a.rendered:
    print(i)

