from poisson_linear import s, u, v, w, J, abc, rank_cert, jacmat, parmat

# component: pullback of a planar pencil foliation times a section O(2,1)
H=(1+u+u**2)+(2+3*u+5*u*u)*v+(7+11*u+13*u*u)*w
Pt=(H,0,0) # alpha=H dw
h_basis=[u**k*coord for k in range(3) for coord in (1,v,w)]
family=[abc(0,0,h) for h in h_basis]
family +=[abc(0,H,0),abc(0,-H*w,H*v)]
assert J(*Pt)==0
print('pencil pullback new: jac rank det, param rank det',rank_cert(jacmat(Pt)),rank_cert(parmat(family)))
assert rank_cert(jacmat(Pt))[0]==23 and rank_cert(parmat(family))[0]==11

# component: a cubic C=LQ with a compatible global projective vector field
L=2*v+3*w+5
Q=2*v*v+v*w+3*w*w+5*v+7*w+11
h=1+2*u+3*u*u
a=7
D=lambda p: (s.diff(p,v),s.diff(p,w))
thetav=L*s.diff(Q,v)-2*Q*s.diff(L,v)
thetaw=L*s.diff(Q,w)-2*Q*s.diff(L,w)
Pt=abc(a*L*Q,h*thetav,h*thetaw)
assert J(*Pt)==0
family=[]
for dl in [1,v,w]:
 da=abc(a*dl*Q,h*(dl*s.diff(Q,v)-2*Q*s.diff(dl,v)),h*(dl*s.diff(Q,w)-2*Q*s.diff(dl,w)))
 family.append(da)
for dq in [1,v,w,v*v,v*w,w*w]:
 family.append(abc(a*L*dq,h*(L*s.diff(dq,v)-2*dq*s.diff(L,v)),h*(L*s.diff(dq,w)-2*dq*s.diff(L,w))))
for dh in [1,u,u*u]:family.append(abc(0,dh*thetav,dh*thetaw))
family.append(abc(L*Q,0,0))
print('line-conic new: jac rank det, param rank det',rank_cert(jacmat(Pt)),rank_cert(parmat(family)))
assert rank_cert(jacmat(Pt))[0]==23 and rank_cert(parmat(family))[0]==11
print('NEW TWO COMPONENT CERTIFICATES VERIFIED')
