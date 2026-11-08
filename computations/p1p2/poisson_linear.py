"""Affine Jacobi equations and exact linearization in the standard bases."""
import sympy as s
u,v,w=s.symbols('u v w')
mon=[v**i*w**j for i in range(4) for j in range(4-i)]
mons=[u**k*v**i*w**j for k in range(3) for i in range(4) for j in range(4-i)]
vec=[(1,0),(0,1),(v,0),(w,0),(0,v),(0,w),(v*v,v*w),(v*w,w*w)]
basis=[(0,0,ff) for ff in mon]+[(u**k*P,u**k*Q,0) for k in range(3) for P,Q in vec]
def J(A,B,C):return s.expand(A*(s.diff(C,v)+s.diff(B,u))+B*(s.diff(C,w)-s.diff(A,u))-C*(s.diff(B,w)+s.diff(A,v)))
def abc(au,av,aw):return tuple(s.expand(t) for t in (aw,-av,au))
def rankmod(M,p=101):
 m=[[int(x)%p for x in row] for row in M];r=0;rows=list(range(len(m))); piv_r=[];piv_c=[]
 for c in range(len(m[0])):
  k=next((i for i in range(r,len(m)) if m[i][c]),None)
  if k is None: continue
  m[k],m[r]=m[r],m[k];rows[k],rows[r]=rows[r],rows[k];piv_r.append(rows[r]);piv_c.append(c)
  inv=pow(m[r][c],-1,p)
  for k in range(r+1,len(m)):
   z=(m[k][c]*inv)%p
   if z:m[k]=[(a-z*b)%p for a,b in zip(m[k],m[r])]
  r+=1
  if r==len(m):break
 return r,piv_r,piv_c
def detmod(M,p=101):
 M=[[int(x)%p for x in row] for row in M];det=1;n=len(M)
 for j in range(n):
  k=next((i for i in range(j,n) if M[i][j]),None)
  if k is None:return 0
  if k!=j:M[k],M[j]=M[j],M[k];det=-det
  z=M[j][j];det=det*z%p;inv=pow(z,-1,p)
  for i in range(j+1,n):
   factor=(M[i][j]*inv)%p
   if factor:M[i]=[(x-factor*y)%p for x,y in zip(M[i],M[j])]
 return det%p
def rank_cert(M):
 r,rs,cs=rankmod(M); d=detmod([[M[i][j] for j in cs] for i in rs]);assert d;return r,d

def jacmat(point):
 A,B,C=point
 polys=[s.Poly(s.expand(J(A+dA,B+dB,C+dC)-J(A,B,C)-J(dA,dB,dC)),u,v,w) for dA,dB,dC in basis]
 return [[p.coeff_monomial(m) for p in polys] for m in mons]
def parmat(vects):
 polys=[tuple(s.Poly(z,u,v,w) for z in vec) for vec in vects]
 return [[ps[i].coeff_monomial(m) for ps in polys] for i in range(3) for m in mons]

