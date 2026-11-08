"""Exact finite checks for the Sklyanin ruling-cover and classical projection examples.

This does not prove the general Smith--Van den Bergh / Tsen statements.
"""
from sympy import symbols, Poly, discriminant, gcd, simplify, expand

x, y, u = symbols('x y u')
f = x**3 - x + 1
assert discriminant(f, x) == -23
assert gcd(Poly(f, x), Poly(f.diff(x), x)).degree() == 0
# The quadratic extension C(x)[y]/(y^2-f(x)) has nontrivial involution.
# A square rational function has even valuation at every zero and pole.
assert Poly(f, x).degree() % 2 == 1  # the branch at infinity
assert simplify((-y)**2 - f - (y**2 - f)) == 0

# The universal inverse for projection from a base point of a pencil of quadrics.
a, b, c, d, e = symbols('a b c d e')
y1, y2, y3, x0 = symbols('y1 y2 y3 x0')
L = (1+u)*y1 + (2-u)*y2 + (u+3)*y3
R = (u+1)*y1*y2 + (2*u-1)*y2*y3 + (u-5)*y1*y3 + y3**2
q = x0*L + R
inverse = {x0: -R, y1: L*y1, y2:L*y2, y3:L*y3}
# Use simultaneous substitution (avoid cascading substitutions)
assert expand(q.subs(inverse, simultaneous=True)) == 0
print('PASS: squarefree elliptic cubic, four-branch double cover, and rational point projection')
