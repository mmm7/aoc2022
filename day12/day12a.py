from input import I,S,E

print(I)
print(S,E)

step = 0
curr=S
vis=set(curr)
ne=[[curr]]

while True:
    step += 1
    candidates = ne.pop(0)
    options = []
    print('==============', step, candidates, ne)
    for ca in candidates:
        for cane in I[ca]:
            print(cane)
            if cane in vis: continue
            vis.add(cane)
            options.append(cane)
            if cane == E:
                print(step)
                exit(0)
    ne.append(options)
    print(ne)
