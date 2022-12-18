from input import I
import math
import time

#print(I)

VECT = [
  (-1,0,0),
  (+1,0,0),
  (0,-1,0),
  (0,+1,0),
  (0,0,-1),
  (0,0,+1)
  ]

res = 0
for x,y,z in I:
  for dx,dy,dz in VECT:
      if (x+dx, y+dy, z+dz) not in I: res+=1

print('A:', res)


mi = [math.inf, math.inf, math.inf]
ma = [math.inf, math.inf, math.inf]

for i in range(3):
    mi[i] = min([x[i] for x in I])
    ma[i] = max([x[i] for x in I])

print(mi)
print(ma)

AIR = set()

for q1 in range(mi[0]-1, ma[0]+2):
  for q2 in range(mi[1]-1, ma[1]+2):
    for q3 in range(mi[2]-1, ma[2]+2):
        if (q1==mi[0]-1 or q1==ma[0]+1 or
            q2==mi[1]-1 or q2==ma[1]+1 or
            q3==mi[2]-1 or q3==ma[2]+1):
            assert((q1,q2,q3) not in I)
            AIR.add((q1,q2,q3))


while True:
    print(len(AIR))
    newair = set()
    for x,y,z in AIR:
        for dx,dy,dz in VECT:
            if (x+dx<mi[0] or x+dx>ma[0] or
                y+dy<mi[1] or y+dy>ma[1] or
                z+dz<mi[2] or z+dz>ma[2]): continue
            if ((x+dx, y+dy, z+dz) not in I and
                (x+dx, y+dy, z+dz) not in AIR):
                newair.add((x+dx, y+dy, z+dz))
    if len(newair) == 0: break
    AIR = AIR.union(newair)

cube,air,trap = 0,0,0
for q1 in range(mi[0]-1, ma[0]+2):
  for q2 in range(mi[1]-1, ma[1]+2):
    for q3 in range(mi[2]-1, ma[2]+2):
        if (q1,q2,q3) in I: cube += 1
        elif (q1,q2,q3) in AIR: air += 1
        else: trap += 1
print(cube,air,trap)

res = 0
for x,y,z in I:
  for dx,dy,dz in VECT:
      if (x+dx, y+dy, z+dz) in AIR: res+=1

print('B:', res)
