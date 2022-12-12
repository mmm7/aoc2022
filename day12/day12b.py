from input import I,SS,E

print(I)
print(SS,E)

step = 0
vis=set(SS)
ne=[SS]

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
