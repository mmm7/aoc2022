from input import I
from operator import add
print(I)

MOVE={
  #(-2,-2): (0,0),
  (-2,-1): (-1,-1),
  (-2, 0): (-1,0),
  (-2,+1): (-1,+1),
  #(-2,+2): (0,0),
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
  #(+2,-2): (0,0),
  (+2,-1): (+1,-1),
  (+2, 0): (+1,0),
  (+2,+1): (+1,+1),
  #(+2,+2): (0,0),
  }

head=[0,0]
tail=(0,0)
ALL=set()
ALL.add(tail)
print(ALL)

for vect,num in I:
    print(vect,num)
    for _ in range(num):
        head = list(map(add,head,vect))
        diff = (head[0]-tail[0], head[1]-tail[1])
        tail = list(map(add,tail,MOVE[tuple(diff)]))
        print(head, diff, tail)
        ALL.add(tuple(tail))


print(ALL)
print(len(ALL))
