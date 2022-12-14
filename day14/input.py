import sys

X=1100
Y=200
I=[['.'] * X for _ in range(Y)]
FLOOR = -1

def cln(s):
    return list(map(int, map(str.strip, s.strip().split(','))))

for line in sys.stdin:
  line = line.strip()
  if not line: continue
  line = line.replace('-', ' ').split('>')
  corn = list(map(cln, line))
  #print(corn)
  x,y=corn[0]
  I[y][x]='#'
  for xt,yt in corn[1:]:
      FLOOR=max(FLOOR,y,yt)
      print(x,y,xt,yt,FLOOR)
      assert x==xt or y==yt
      #print(x, y, 'lineto', xt,yt)
      if x==xt:
          for yyy in range(min(y,yt), max(y,yt)+1):
              I[yyy][x] = '#'
              #print('yyy',x,yyy)
      else:
          for xxx in range(min(x,xt), max(x,xt)+1):
              I[y][xxx] = '#'
              #print('xxx', xxx,y)
      x,y = xt,yt
FLOOR+=2

