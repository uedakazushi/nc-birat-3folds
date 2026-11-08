"""Four-factor logarithmic family. All ranks and invariant factors are exact."""
import sympy as s
from sympy.matrices.normalforms import smith_normal_form
from poisson_linear import u, v, w, J, abc, jacmat, parmat


def four_form(factors, a, b):
    residues = (a, -a, b, -a-b)
    return abc(*(sum(residues[i] * s.diff(factors[i], z)
                     * s.prod(factors[:i] + factors[i+1:]) for i in range(4))
                 for z in (u, v, w)))


base = [u+v+w, 1, v, w]
r = s.Symbol('r')
point = four_form(base, 1, r)
assert J(*point) == 0
matrix = s.Matrix(jacmat(point))
rank_at = lambda x: matrix.subs(r,x).rank()
assert rank_at(2) == 22
directions = []
linear = [1, v, w]
for i, basis in enumerate(([1,v,w,u,u*v,u*w], [1,u], linear, linear)):
    for section in basis:
        factors = base.copy()
        factors[i] = section
        directions.append(four_form(factors, 1, 2))
directions.extend((four_form(base, 1, 0), four_form(base, 0, 1)))
assert s.Matrix(parmat(directions)).rank() == 12
print("family rank 12, Jacobi rank 22 at r=2 (Q)")

ring = s.QQ.poly_ring(r)
smith = smith_normal_form(matrix, domain=ring)
invariants = [s.Poly(z, r).monic().as_expr() for z in smith.diagonal() if z != 0]
f = (r-1)*(r+2)
g = r*(r+1)*(r+s.Rational(1,2))
expected = [1]*19 + [f, f, f*g]
assert len(invariants) == len(expected)
assert all(s.expand(x-y)==0 for x, y in zip(invariants, expected))
assert s.Matrix(jacmat(four_form(base, 0, 1))).rank() == 20
print("Smith invariants over Q[r] verified; Jacobi rank 20 at infinity")
