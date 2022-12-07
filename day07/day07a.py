from input import I

print(I)

dirs={}

pwd = []

def dirn(l):
    return '/'.join(l)

def parsedir(D, p):
    #print('===>', D, p)
    s = 0
    for k,v in D.items():
        #print(k,v)
        if isinstance(v, dict):
            s+=parsedir(v, p+[k])
        else:
            s+=v
    dirs[dirn(p)] = s
    return s

parsedir(I, [''])
print(dirs)

s = 0
for k,v in dirs.items():
    if v<=100000: s+=v

print('=========DAY1:',s)

freespace = 70000000 - dirs['//']
print('freespace:', freespace)
required = 30000000 - freespace
print('required:', required)

best = 700000000
for k,v in dirs.items():
    if v<required: continue
    if v<best: best = v

print('=========DAY2:',best)
