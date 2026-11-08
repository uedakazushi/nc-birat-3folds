"""Check Jacobian linearization at toric Poisson point on P1 x P2.
Requires Python 3 and SymPy. This is an independent computational check,
not a replacement for the direct monomial proof in the TeX manuscript.
"""
import sympy as s
u, v, w = s.symbols('u v w')
mon = [v**i*w**j for i in range(4) for j in range(4-i)]
vector_fields = [
    (1, 0), (0, 1), (v, 0), (w, 0), (0, v), (0, w),
    (v**2, v*w), (v*w, w**2)
]
basis = [(0, 0, f) for f in mon]
basis += [(u**k * P, u**k * Q, 0) for k in range(3) for P, Q in vector_fields]
A, B, C = 2*u*v, 3*u*w, 5*v*w

def jac(A, B, C):
    return s.expand(A*(s.diff(C, v)+s.diff(B, u))
        + B*(s.diff(C, w)-s.diff(A, u))
        - C*(s.diff(B, w)+s.diff(A, v)))

def lin(dA, dB, dC):
    return s.expand(jac(A+dA, B+dB, C+dC)-jac(A, B, C)-jac(dA, dB, dC))

mons = [u**k*v**i*w**j for k in range(3) for i in range(4) for j in range(4-i)]
M = s.Matrix([[s.Poly(lin(*b), u, v, w).coeff_monomial(m) for b in basis] for m in mons])
assert len(basis) == 34 and len(mons) == 30
assert jac(A, B, C) == 0
assert M.rank() == 23
print('basis=34, Jacobi equations=30, Jacobian rank=23, tangent dim=11: verified')
