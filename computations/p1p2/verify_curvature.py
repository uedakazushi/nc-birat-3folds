"""Symbolic curvature identities in a chart where one polar line is logarithmic.

The five choices exhaust the affine conic types used in the normal-form
proofs. Universal traceless matrices are used (no numeric specialization).
"""
import sympy as s

x, y = s.symbols("x y")


def matrix(name):
    u, v, w = s.symbols(f"{name}0:3")
    return s.Matrix([[u, v], [w, -u]])


def bracket(U, V):
    return U*V - V*U


A, B, C, D, E, G = map(matrix, "ABCDEG")
X, Y = A+B*x+C*y, D+E*x+G*y

for name, q, expected in [
    ("secant", x*y-1, [C-E, A, -D, B, s.zeros(2), -G]),
    ("triangle", x*y, [s.zeros(2), A, -D, B, s.zeros(2), -G]),
    ("tangent", y-x*x, [A, 2*D+B, E, E+C, 2*G, s.zeros(2)]),
    ("concurrent", x*(x-1), [D, C-2*D, G, -E-C, -2*G, s.zeros(2)]),
    ("double", x*x, [s.zeros(2), -2*D, s.zeros(2), -E-C, -2*G, s.zeros(2)]),
]:
    monomials = (1, x, y, x*x, x*y, y*y)
    derivative_part = q*(E-C)-s.diff(q,x)*Y+s.diff(q,y)*X
    derivative_target = sum((m*c for m,c in zip(monomials,expected)),s.zeros(2))
    assert (derivative_part-derivative_target).applyfunc(s.expand) == s.zeros(2), name

commutators = [bracket(A,D), bracket(A,E)+bracket(B,D), bracket(A,G)+bracket(C,D),
               bracket(B,E), bracket(B,G)+bracket(C,E), bracket(C,G)]
target = sum((m*c for m,c in zip(monomials,commutators)),s.zeros(2))
assert (bracket(X,Y)-target).applyfunc(s.expand) == s.zeros(2)
print("Five affine curvature coefficient tables verified symbolically.")
