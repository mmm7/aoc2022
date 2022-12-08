from input import I

print(I)

visible = 0
h=-1
v=-1

print(len(I), len(I[0]))

def view(coord, vect):
    x,y = coord
    cur = I[y][x]
    xx,yy = x,y
    score = 0
    while True:
        xx+=vect[0]
        yy+=vect[1]
        if yy<0 or yy>=len(I) or xx<0 or xx>=len(I[0]): break
        score += 1
        if I[yy][xx] >= cur: break
    return score

best=0
for y in range(len(I)):
    for x in range(len(I[0])):
        curr = (
          view((x,y),(-1,0)) *
          view((x,y),(+1,0)) *
          view((x,y),(0,-1)) *
          view((x,y),(0,+1)))
        print(y,x,curr)
        if curr > best: best = curr

print(best)

