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


def profilehash(p, curr, windp, h):
    return tuple([curr,windp] + [h-x for x in p])

curr = -1
windp = -1

profile = [0,0,0,0,0,0,0,0,0]

profiles = {}

cycle = 1000000000000
additional = 0

while True:
  cycle-=1
  if cycle<0: break
  if cycle % 10000 == 0: print(cycle, len(profiles))
  #deb()
  #time.sleep(1)
  he = height(pit)

  #profiles
  ph = profilehash(profile,curr,windp,he)
  if ph in profiles:
      oc, oh = profiles[ph]
      cyclelen=oc-cycle
      heightdiff = he-oh
      print((oc,oh), (cycle,he), '->', cyclelen, heightdiff)
      if cycle > cyclelen:
          additional = (cycle // cyclelen) * heightdiff
          cycle %= cyclelen
          print('=============NOW=>', additional, cycle)
  profiles[ph] = (cycle,he)

  for _ in range(10-len(pit)+he): pit.append(PITL)
  x=3
  y=he+4

  curr = (curr+1) % len(P)
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
        li = P[curr][yy] << x
        pit[y+yy] |= li
        for bit in range(9):
            if pit[y+yy] & (1<<bit): profile[bit] = y+yy
    break


print("B:", height(pit)+additional)
