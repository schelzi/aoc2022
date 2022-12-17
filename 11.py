import yaml
import math

class Monkey:
    def __init__(self, name, features):
        self.items = [int(item) for item in str(features['Starting items']).split(',')]
        # self.op = 'setattr('+name+',new,eval('+features['Operation'].split('=')+'))'
        self.op = ''.join(features['Operation'].split('=')[1])
        self.t = features[True]
        self.f = features[False]
        self.test = features['Test']
        self.action_count = 0
        
    
    def sling(self, item):
        old = item 
        self.action_count += 1
        # worry = eval(self.op) // 3
        worry = eval(self.op) % lcm
        if worry % self.test == 0:
            monkeys[self.t].get(worry)
        else:
            monkeys[self.f].get(worry)
        self.items.remove(item)


    def turn(self):
        tmp = list(self.items)
        for item in tmp:
            self.sling(item)
    
    def get(self, item):
        self.items.append(item)

    




with open('11a.yaml','r') as f:
    data = yaml.safe_load(f)
print(data)

monkeys = {}
lcm = 1
# lcm keeps the numbers relatively small, because it modulos the item values by the product of all prime divisors divided by the greatest common divisor of all primes
# which is optional though. works with the product solely, too
for monkey in data:
    monkeys[monkey] = Monkey('monkeys['+str(monkey)+']',data[monkey])
    lcm *= (lcm*monkeys[monkey].test)#//math.gcd(lcm,monkeys[monkey].test)


for i in range(10000):
    print(i)
    for monkey in monkeys:
        monkeys[monkey].turn()

monkeyness = (sorted([monkeys[monkey].action_count for monkey in monkeys],reverse=True)[:2])
print(monkeyness[0]*monkeyness[1])