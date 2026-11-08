"""Exact/checkable symbolic certificates for the del Pezzo components of
Pois(P^1 x P^2), revision 2.0 (2026-11-06).

Requires only Python 3 and SymPy. In particular, numerical ranks are computed
over F_101, which certifies LOWER bounds for rational matrix ranks.
The component proof uses the matching parameter rank and Jacobi rank bounds.
"""
import sympy as s

u,v,w=s.symbols('u v w')
mon=[v**i*w**j for i in range(4) for j in range(4-i)]
mons=[u**k*v**i*w**j for k in range(3) for i in range(4) for j in range(4-i)]
vec=[(1,0),(0,1),(v,0),(w,0),(0,v),(0,w),(v*v,v*w),(v*w,w*w)]
basis=[(0,0,ff) for ff in mon]+[(u**k*P,u**k*Q,0) for k in range(3) for P,Q in vec]
assert len(basis)==34 and len(mons)==30

def abc(au,av,aw):
    # If alpha=au du+av dv+aw dw, then alpha=i_pi(du^dv^dw)
    # for pi=A du^dv+B du^dw+C dv^dw.
    return tuple(s.expand(aa) for aa in (aw,-av,au))

def J(A,B,C):
    return s.expand(A*(s.diff(C,v)+s.diff(B,u))
        +B*(s.diff(C,w)-s.diff(A,u))-C*(s.diff(B,w)+s.diff(A,v)))

def abc_dp5(F,H):
    # deg(F)=(1,2), deg(H)=(1,1)
    return abc(H*s.diff(F,u)-F*s.diff(H,u),
               H*s.diff(F,v)-2*F*s.diff(H,v),
               H*s.diff(F,w)-2*F*s.diff(H,w))

def abc_dp8a(F,U,Q):
    # deg(F)=(1,1), deg(U)=(1,0), deg(Q)=(0,2)
    return abc(2*U*Q*s.diff(F,u)-2*F*Q*s.diff(U,u),
               2*U*Q*s.diff(F,v)-F*U*s.diff(Q,v),
               2*U*Q*s.diff(F,w)-F*U*s.diff(Q,w))

def abc_dp8b(F,G,L):
    # deg(F)=deg(G)=(1,1), deg(L)=(0,1)
    return abc(L*(G*s.diff(F,u)-F*s.diff(G,u)),
               L*(G*s.diff(F,v)-F*s.diff(G,v)),
               L*(G*s.diff(F,w)-F*s.diff(G,w)))

def rankmod(M,p=101):
    M=[[int(x)%p for x in row] for row in M]
    r=0;nr=len(M);nc=len(M[0]);piv=[]
    for c in range(nc):
        i=next((i for i in range(r,nr) if M[i][c]),None)
        if i is None: continue
        M[i],M[r]=M[r],M[i]
        inv=pow(M[r][c],-1,p)
        M[r]=[z*inv%p for z in M[r]]
        for k in range(r+1,nr):
            z=M[k][c]
            if z: M[k]=[(a-z*b)%p for a,b in zip(M[k],M[r])]
        piv.append(c);r+=1
        if r==nr:break
    return r,piv

def jacobi_derivative_matrix(point):
    A,B,C=point
    polys=[]
    for dA,dB,dC in basis:
        # Bilinear (polarized) Jacobi equation
        jac=s.expand(J(A+dA,B+dB,C+dC)-J(A,B,C)-J(dA,dB,dC))
        polys.append(s.Poly(jac,u,v,w).as_dict())
    return [[int(d.get((k,i,j),0)) for d in polys]
        for k in range(3) for i in range(4) for j in range(4-i)]

def parameter_derivative_matrix(vectors):
    columns=[]
    for A,B,C in vectors:
        columns.append([int(s.Poly(P,u,v,w).coeff_monomial(m))
                        for P in (A,B,C) for m in mons])
    return [list(row) for row in zip(*columns)]

f11=[u**k*t for k in (0,1) for t in (1,v,w)]
f12=[u**k*v**i*w**j for k in (0,1) for i in range(3) for j in range(3-i)]
u10=[1,u]
l01=[1,v,w]
q02=[v**i*w**j for i in range(3) for j in range(3-i)]

# Fixed-S classification in bidegree (1,2)
a=s.symbols('a0:6')
F=u*v*w+(v-1)*(w-1)
H=(a[0]+a[1]*v+a[2]*w)+u*(a[3]+a[4]*v+a[5]*w)
m01=a[0]*a[4]-a[1]*a[3]
m02=a[0]*a[5]-a[2]*a[3]
m12=a[1]*a[5]-a[2]*a[4]
A,B,C=abc_dp5(F,H)
assert s.expand(J(A,B,C)-F*(m01*((u+1)*v-1)
                              -m02*((u+1)*w-1)-m12*(v+w-2)))==0
print('fixed (1,2) divisor: Jacobi=F*(linear combination of three 2x2 minors): verified')

# Component witnesses. Jacobian/parameter ranks over F_101 suffice to
# show rank in characteristic 0 is at least the displayed number.
F5=F;U5=2*u+3;L5=v+2*w+1
P5=abc_dp5(F5,U5*L5)
para5=[abc_dp5(ff,U5*L5) for ff in f12]
para5 +=[abc_dp5(F5,uu*L5) for uu in u10]
para5 +=[abc_dp5(F5,U5*ll) for ll in l01]

F8=u*v+w
U8=2*u+3
Q8=2*v*v+v*w+3*w*w+5*v+7*w+11
P8a=abc_dp8a(F8,U8,Q8)
para8a=[abc_dp8a(ff,U8,Q8) for ff in f11]
para8a +=[abc_dp8a(F8,uu,Q8) for uu in u10]
para8a +=[abc_dp8a(F8,U8,qq) for qq in q02]

F8b=(u+1)*(v+2*w+1)+(2*u+3)*(2*v-w+3)
G8b=(3*u+1)*(v+3*w+2)+(u+4)*(2*v+w+5)
L8b=2*v+3*w+5
P8b=abc_dp8b(F8b,G8b,L8b)
para8b=[abc_dp8b(ff,G8b,L8b) for ff in f11]
para8b +=[abc_dp8b(F8b,gg,L8b) for gg in f11]
para8b +=[abc_dp8b(F8b,G8b,ll) for ll in l01]

for name,point,parameters,expected in [
        ('(1,2)+(1,0)+(0,1)',P5,para5,14),
        ('(1,1)+(1,0)+(0,2)',P8a,para8a,12),
        ('(1,1)+(1,1)+(0,1)',P8b,para8b,11)]:
    assert J(*point)==0
    rkJ,cJ=rankmod(jacobi_derivative_matrix(point))
    rkP,cP=rankmod(parameter_derivative_matrix(parameters))
    assert rkJ==34-expected and rkP==expected
    print('%s: Jacobi rank>=%s, parameter rank>=%s, dim=%s: verified (mod 101)' %
          (name,rkJ,rkP,expected))
print('All certificates passed')
