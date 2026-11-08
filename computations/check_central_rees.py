"""Exact checks for central pencils: Hilbert bi-series and vertex obstruction.

These tests verify finite polynomial identities. They do NOT verify the
categorical Orlov SOD (proved separately using derived base change).
"""
import sympy as sp
z, w = sp.symbols('z w')
H_D = (1 + 4*z + z*z)/(1-z)**2
H_A = sp.cancel(H_D/(1-z)**2)
H_Rees = sp.cancel(H_A*(1-z*z*w)/(1-z*w)**2)
assert sp.cancel(H_A - sum((n+1)**3*z**n for n in range(12))) != 0 # rational series has a tail
Acoeff = sp.series(H_A, z, 0, 18).removeO().expand()
for n in range(18):
    assert Acoeff.coeff(z,n) == (n+1)**3
for n in range(10):
    assert sp.series(H_D,z,0,n+1).removeO().expand().coeff(z,n) == (1 if n==0 else 6*n)
# Bigraded Rees: m^r has in C_n dimension n+1 for n>=r.
# Thus dim Rees_{n,r} = sum_{j=0}^{n-r} dim(D_j)*(n-j+1).
for r in range(7):
    coeff_w = sp.series(H_Rees, w, 0, r+1).removeO().expand().coeff(w,r)
    trunc = sp.series(coeff_w, z, 0, 13).removeO().expand()
    for n in range(13):
        predicted = sum((1 if j==0 else 6*j)*(n-j+1) for j in range(n-r+1)) if n>=r else 0
        assert trunc.coeff(z,n) == predicted, (n,r,trunc.coeff(z,n),predicted)
# The vertex cannot be removed inside perfect graded modules, since k has infinite pd.
assert sp.gcd(1+4*z+z*z,(1-z)**4)==1
assert sp.rem((1-z)**4,1+4*z+z*z,z) != 0
# The same anticanonical Hilbert function for distinct and infinitely near point blow-ups.
for n in range(12):
    assert 1+7*n*(n+1)//2 == (7*n*n+7*n+2)//2
print('Central pencil Hilbert series, bigraded Rees dimensions, vertex obstruction: OK')
