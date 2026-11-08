import sympy as s
u,v,w=s.symbols('u v w')
F=u*v+w
a0,a1,b0,b1,b2,c0,c1,c2,c3=s.symbols('a0 a1 b0 b1 b2 c0 c1 c2 c3')
x0,x1,y0,y1,z0,z1=s.symbols('x0 x1 y0 y1 z0 z1')
pars=[a0,a1,b0,b1,b2,c0,c1,c2,c3,x0,x1,y0,y1,z0,z1]
H=a0+a1*u+v*(b0+b1*u)+b2*u*w+v*v*(c0+c1*u)+c2*u*v*w+c3*u*w*w
gv=x0+x1*u-(z0+z1*u)*w
gw=y0+y1*u+(z0+z1*u)*v
alpha=[2*H*s.diff(F,u)-2*F*s.diff(H,u), 2*H*s.diff(F,v)-F*s.diff(H,v)+F*gv,2*H*s.diff(F,w)-F*s.diff(H,w)+F*gw]
A,B,C=alpha[2],-alpha[1],alpha[0]
J=s.expand(A*(s.diff(C,v)+s.diff(B,u))+B*(s.diff(C,w)-s.diff(A,u))-C*(s.diff(B,w)+s.diff(A,v)))
P=s.Poly(s.div(J,F,w)[0],u,v,w);assert s.rem(J,F,w)==0
cs={m:p for m,p in P.terms()}
assert len(cs)==12
vec=[(1,0),(0,1),(v,0),(w,0),(0,v),(0,w),(v*v,v*w),(v*w,w*w)]
mon=[v**i*w**j for i in range(4) for j in range(4-i)]
basis=[(0,0,ff) for ff in mon]+[(u**k*P,u**k*Q,0) for k in range(3) for P,Q in vec]
red=[]
for a,b,c in basis:
  p1=s.expand((c-v*a).subs(w,-u*v));p2=s.expand((b+u*a).subs(w,-u*v));red.append((p1,p2))
monuv=sorted({m for p1,p2 in red for p in (p1,p2) for m in s.Poly(p,u,v).monoms()})
M=s.Matrix([[int(s.Poly(p[i],u,v).coeff_monomial(u**k*v**j)) for p in red] for i in range(2) for k,j in monuv]);print('tangency rank, solution dim:',M.rank(),34-M.rank());assert M.rank()==19
# sample tensors rank
imgs=[]
for z in pars:
  vals={a:0 for a in pars};vals[z]=1
  imgs.append(tuple(s.expand(q.subs(vals)) for q in (A,B,C)))
monuvws=sorted({m for img in imgs for p in img for m in s.Poly(p,u,v,w).monoms()})
N=s.Matrix([[int(s.Poly(img[i],u,v,w).coeff_monomial(u**k*v**j*w**l)) for img in imgs] for i in range(3) for k,j,l in monuvws]);print('param rank:',N.rank());assert N.rank()==15
nodal={a0:0,a1:0,b0:0,b1:1,b2:0}
cusp={a0:0,a1:0,b0:1,b1:0,b2:0}
nodeconds=[((0,1,0),2*x0),((1,0,1),-2*y1),((1,1,0),x0*y1-(x1+1)*y0),((0,2,0),2*(c0*(1-x1+2*y0)+c1*x0)),((1,0,2),2*(-c2*y1+c3*(2*x1-y0)))]
for m,p in nodeconds:assert s.expand(cs[m].subs(nodal)-p)==0
cuspconds=[((0,1,0),-2*(x1-y0)),((1,1,0),x0*y1-x1*y0+3*y1),((0,0,1),x0*y1-x1*y0-y1),((0,0,2),-c2*y0+4*c3*x0+y0*z1-y1*z0),((1,1,1),-4*c1*y1+2*c2*x1-c2*y0-2*c3*x0+2*c3+y0*z1-y1*z0)]
for m,p in cuspconds:assert s.expand(cs[m].subs(cusp)-p)==0
zero={a:0 for a in [a0,a1,b0,b1,b2,c0,c1,c2,c3]}
for m,p in cs.items():
  pp=s.expand(p.subs(zero))
  assert pp in [0, x0*z1-x1*z0, y0*z1-y1*z0, x0*y1-x1*y0]
print('nodal/cusp necessary coefficients and beta=0 rank-one constraints: verified')
