"""An obstructed first-order direction at a point of the concurrent Riccati family."""
from poisson_linear import s, u as t, v as x, w as y, J, jacmat, mons

roots = (0, 1, 2)
f = s.prod(x-i for i in roots)
h = 1+2*t+3*t**2 + x*(4+7*t+11*t**2)
P = s.expand(s.interpolate([(i,-h.subs(x,i)/s.diff(f,x).subs(x,i)) for i in roots], x))
c = P.coeff(x,2)
d = s.cancel(((s.diff(f,x)+s.diff(h,t))*P-h*s.diff(P,t)-f*(s.diff(P,x)+c*x)+h)/f)
base = (0,h,f)
delta = (P,y*(d+c*x),y)
linear = s.expand(J(*(a+b for a,b in zip(base,delta))) - J(*base) - J(*delta))
assert linear == 0
matrix = s.Matrix(jacmat(base))
quadratic = s.Poly(J(*delta),t,x,y)
obstruction = s.Matrix([quadratic.coeff_monomial(m) for m in mons])
assert (matrix.rank(),matrix.row_join(obstruction).rank()) == (21,22)

# Explicit certificate printed in the main manuscript.
weights = ((886, -739, 61), (-1521, 279, -171), (756, 81, 81))
functional = s.zeros(1, len(mons))
for k in range(3):
    for i in range(3):
        functional[0, mons.index(t**k*x**i*y)] = weights[k][i]
assert functional*matrix == s.zeros(1, matrix.cols)
assert (functional*obstruction)[0] == -72900

rows = (1, 2, 3, 5, 6, 8, 9, 10, 11, 12, 15, 16, 18, 19, 20, 21, 22, 25, 26, 28, 30)
columns = (2, 3, 4, 6, 7, 9, 11, 13, 14, 16, 17, 18, 19, 21, 22, 24, 25, 26, 27, 30, 34)
minor = matrix[[i-1 for i in rows], [j-1 for j in columns]]
assert minor.det() == -2**19*3**13*5**2*11*19
print("First order verified. Exact Jacobi/augmented ranks over Q: 21, 22.")
print("Printed obstruction functional and rank-21 minor verified exactly.")
