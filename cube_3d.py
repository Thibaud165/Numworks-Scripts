from math import *
from ion import *
from kandinsky import *

CD=[[-50+100*int(e) for e in list(bin(j)[3:])] for j in [77,111,72,108,123,89,68,102,126,90,114,80]]
MS,RS,P,W,H,C,L,S,F0,RA=5,0.05,50,320,222,[0,0,300,0,0,0],[(0,0,0),(255,255,255)],[],False,True
KD={0:(0,-MS),3:(0,MS),1:(1,-MS),2:(1,MS),45:(2,MS),46:(2,-MS),30:(3,-RS),31:(4,-RS),32:(5,-RS),42:(3,RS),43:(4,RS),44:(5,RS)}
_X=lambda x,y,z:_Y(x,y*cos(C[3])-z*sin(C[3]),z*cos(C[3])+y*sin(C[3]))
_Y=lambda x,y,z:_Z(x*cos(C[4])-z*sin(C[4]),y,z*cos(C[4])+x*sin(C[4]))
_Z=lambda x,y,z:_P(x*cos(C[5])-y*sin(C[5]),y*cos(C[5])+x*sin(C[5]),z)
_P=lambda x,y,z:[(C[2]*(x+C[0]))/(C[2]+z)+C[0]+W//2,(C[2]*(y+C[1]))/(C[2]+z)+C[1]+H//2]
# RA=False pour ancienne méthode de render

def line(x1,y1,z1,x2,y2,z2,p):
  x1,y1=_X(x1,y1,z1)
  x2,y2=_X(x2,y2,z2)
  cx,cy,mx,my=(x1-x2)/p,(y1-y2)/p,x2,y2
  for i in range(p+1):
    S.append((int(mx),int(my))) if RA else set_pixel(int(mx),int(my),L[0])
    mx,my=mx+cx,my+cy

def render(d,c=0):
  for e in d:
    set_pixel(e[0],e[1],L[c])

while True:
  for l in CD:
    if RA:
      render(S[0:P+1],1)
      if F0: del S[:P+1]
    line(*l,p=P)
    RA and render(S[-(P+1):-1])
  not RA and fill_rect(0,0,W,H,L[1])
  F0=True
  for k in KD.keys():
    if keydown(k): C[KD[k][0]]+=KD[k][1]
  C[4] += RS
  C[5] -= RS
