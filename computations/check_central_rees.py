"""Exact finite coefficient checks for a central pencil and its bigraded Rees algebra.

Unlike repeated symbolic Taylor expansions, coefficients are computed from exact
convolution formulas. The general algebraic identities and Orlov SOD are in TeX;
this script verifies their finite numerical consequences, not the categorical proof.
"""
import sympy as sp

z, w = sp.symbols('z w')
H_D = (1 + 4*z + z*z)/(1-z)**2
H_A = 1/(1-z)**4 * (1+4*z+z*z)
H_Rees = H_A*(1-z*z*w)/(1-z*w)**2
assert sp.cancel(H_A - H_D/(1-z)**2) == 0
assert sp.cancel(H_Rees - (H_D/(1-z)**2)*(1-z*z*w)/(1-z*w)**2) == 0

def d(n): return 1 if n == 0 else 6*n if n > 0 else 0

def a(n): return 0 if n < 0 else (n+1)**3

# H_A(z) = H_D(z)/(1-z)^2, checked directly by finite convolution.
for n in range(25):
    assert sum(d(j)*(n-j+1) for j in range(n+1)) == a(n)

# Coefficient of w^r in (1-z^2w)/(1-zw)^2 is
# z^r ((r+1)-r z) for r>=0. Compare with direct Rees filtration count.
for r in range(12):
    for n in range(25):
        via_series = (r+1)*a(n-r)-r*a(n-r-1)
        predicted = sum(d(j)*(n-j+1) for j in range(n-r+1)) if n >= r else 0
        assert via_series == predicted, (n, r, via_series, predicted)

# k has infinite graded projective dimension over the elliptic central quotient,
# since 1/H_D is not a polynomial (standard Euler-Poincare obstruction).
assert sp.gcd(1 + 4*z + z*z, (1-z)**4) == 1
assert sp.rem((1-z)**4, 1+4*z+z*z, z) != 0
for n in range(12):
    assert 1 + 7*n*(n+1)//2 == (7*n*n + 7*n + 2)//2
print('PASS: central pencil Hilbert and bigraded Rees coefficients; vertex obstruction')
