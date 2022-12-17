from input import I,P
import time

PITL=0b100000001

print(P)
print(I)

pit = [0b111111111]

pc=0

def height(pi):
    for y in range(len(pi)-1, -1, -1):
        if pi[y]!=PITL: return y

assert height([0b111111111]) == 0
assert height([0b111111111, PITL, PITL]) == 0
assert height([0b111111111, 0b10000101, 0b0100001, PITL, PITL]) == 2

def overlap(pi, piece, x, y):
    for yy in range(len(piece)):
        patt=piece[yy] << x
        if pit[y+yy] & patt: return True
    return False

def deb():
    global pit
    print('==============================')
    for l in pit:
        print(bin(l))

curr = -1
windp = -1

cycle = 2022
while True:
  cycle-=1
  if cycle<0: break
  #deb()
  #time.sleep(1)
  curr = (curr+1) % len(P)
  he = height(pit)
  for _ in range(10-len(pit)+he): pit.append(PITL)
  x=3
  y=he+4
  assert not overlap(pit, P[curr], x,y)

  # Fall:
  while True:
    windp = (windp+1) % len(I)
    wi=I[windp]
    assert wi==1 or wi==-1
    if not overlap(pit, P[curr], x+wi, y): x=x+wi
    if not overlap(pit, P[curr], x, y-1):
        y = y-1
        continue
    # Freeze
    assert not overlap(pit, P[curr], x,y)
    for yy in range(len(P[curr])):
        pit[y+yy] |= P[curr][yy] << x
    break


print("A:", height(pit))
