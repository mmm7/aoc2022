from input import I

print(I)

# items, mul, add, test, tt, tf = [], 1, 0, 0, 0, 0
# I.append([items, (mul, add), (test, tt, tf)])

act = [0] * len(I)

def round():
    global I
    for m in range(len(I)):
        itemnum = len(I[m][0])
        for _ in range(itemnum):
            act[m] += 1
            item = I[m][0].pop(0)
            mul, add = I[m][1]
            test,tt,tf = I[m][2]
            if mul is None: mul = item
            if add is None: add = item
            item = item * mul + add
            item //= 3

            target = tf
            if item % test == 0: target = tt
            I[target][0].insert(0,item)
            
        print(m,I)

for r in range(20):
    print('==========', r)
    round()

act.sort()
print(act)
print(act[-1] * act[-2])
