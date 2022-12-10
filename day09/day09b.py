from input import I
from operator import add
print(I)

MOVE={
  (-2,-2): (-1,-1),
  (-2,-1): (-1,-1),
  (-2, 0): (-1,0),
  (-2,+1): (-1,+1),
  (-2,+2): (-1,+1),
  (-1,-2): (-1,-1),
  (-1,-1): (0,0),
  (-1, 0): (0,0),
  (-1,+1): (0,0),
  (-1,+2): (-1,+1),
  ( 0,-2): (0,-1),
  ( 0,-1): (0,0),
  ( 0, 0): (0,0),
  ( 0,+1): (0,0),
  ( 0,+2): (0,+1),
  (+1,-2): (+1,-1),
  (+1,-1): (0,0),
  (+1, 0): (0,0),
  (+1,+1): (0,0),
  (+1,+2): (+1,+1),
  (+2,-2): (+1,-1),
  (+2,-1): (+1,-1),
  (+2, 0): (+1,0),
  (+2,+1): (+1,+1),
  (+2,+2): (+1,+1),
  }

rope=[(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),(0,0),]
ALL=set()
print(rope)
ALL.add(rope[9])
print(ALL)

for vect,num in I:
    print(vect,num)
    for _ in range(num):
        rope[0] = list(map(add,rope[0],vect))
        for r in range(9):
            diff = (rope[r][0]-rope[r+1][0], rope[r][1]-rope[r+1][1])
            rope[r+1] = list(map(add,rope[r+1],MOVE[tuple(diff)]))
            ALL.add(tuple(rope[9]))
        print(rope)


print(ALL)
print(len(ALL))
