"""Exact checks for the P3 exceptional and differential-Ore charts. 2026-11-07."""
import sympy as sp

z1, z2, z3, h = sp.symbols('z1 z2 z3 h')
variables = (z1, z2, z3)

def vector_field(coefficients, f):
    return sp.expand(sum(a * sp.diff(f, z) for a, z in zip(coefficients, variables)))

def X(f):
    return vector_field((z1, 2*z2, 3*z3), f)

def Y(f):
    return vector_field((4, 4*z1, 4*z2), f)

def star(f, g):
    result = sp.expand(f*g)
    derivative = f
    falling = g
    k = 1
    while True:
        derivative = Y(derivative)
        if derivative == 0:
            break
        falling = sp.expand((X(falling) - (k-1)*falling) / k)
        result += h**k * derivative * falling
        k += 1
    return sp.expand(result)

s = z1 / 4
p = z2 - z1**2 / 2
q = z3 - z1*z2 + z1**3 / 3
for f in variables:
    assert sp.expand(Y(X(f)) - X(Y(f)) - Y(f)) == 0
assert Y(s) == 1 and Y(p) == 0 and Y(q) == 0
assert X(s) == s and sp.expand(X(p)-2*p) == 0 and sp.expand(X(q)-3*q) == 0
assert sp.expand(star(s,p)-star(p,s)-2*h*p) == 0
assert sp.expand(star(s,q)-star(q,s)-3*h*q) == 0
assert sp.expand(star(p,q)-star(q,p)) == 0
for a,b,c0 in ((z1,z2,z3),(s,p,q),(z2,z3,z1)):
    assert sp.expand(star(star(a,b),c0)-star(a,star(b,c0))) == 0
P0,Q0,R0,C0 = sp.symbols('p q r c', nonzero=True)
delta = lambda f: sp.simplify(2*P0*sp.diff(f,P0) + 3*Q0*sp.diff(f,Q0))
r = Q0/P0
c = Q0**2/P0**3
assert delta(r) == r and delta(c) == 0
assert sp.simplify((r**2/c)-P0) == 0
assert sp.simplify((r**3/c)-Q0) == 0
print('PASS: exceptional CGG relations, sampled associativity, Weyl rational change')

x1,x2,x3,v,w = sp.symbols('x1 x2 x3 v w', nonzero=True)
a = sp.symbols('a0:18')
monomials = (x1*x1,x1*x2,x1*x3,x2*x2,x2*x3,x3*x3)
F = [sum(a[6*i+j]*m for j,m in enumerate(monomials)) for i in range(3)]
d = lambda f: sum(fi*sp.diff(f,xi) for fi,xi in zip(F,(x1,x2,x3)))
for i,var in enumerate((x1,x2)):
    actual = sp.cancel(d(var/x3)/x3).subs({x1:v*x3,x2:w*x3})
    expected = (F[i]- (v,w)[i]*F[2]).subs({x1:v,x2:w,x3:1})
    assert sp.simplify(actual-expected) == 0
print('PASS: general homogeneous quadratic differential-Ore dehomogenization')
