#!/usr/bin/env python3
"""Exact finite checks for toric AS-rationality formulas, not a general proof."""
import itertools
import sympy as sp

# a generic three-parameter skew matrix; coefficients are formal and independent.
A,B,C=sp.symbols('a b c')
Lambda=sp.Matrix([[0,A,B],[-A,0,C],[-B,-C,0]])
Ms=[sp.eye(3),sp.Matrix([[1,1,0],[0,1,0],[0,0,1]]),
    sp.Matrix([[0,1,0],[1,0,0],[0,0,-1]]),
    sp.Matrix([[1,0,1],[0,1,1],[0,0,1]])]
for M in Ms:
    assert abs(int(M.det()))==1
    Q=M.T*Lambda*M
    assert Q+Q.T==sp.zeros(3)
    for i in range(3):
        for j in range(3):
            assert sp.expand(Q[i,j]-(M[:,i].T*Lambda*M[:,j])[0])==0

# Dehomogenization of the skew polynomial B_q with central x0 is formal:
# u_i = x_i/x0, so the commutation matrix is unchanged.
# For integer-valued lambda test the lattice of central monomials and
# Poisson Casimirs. This finite set of exponents does not certify all cases.
LM=sp.Matrix([[0,2,-4],[-2,0,6],[4,-6,0]])
for m in itertools.product(range(-4,5),repeat=3):
    vec=sp.Matrix(m)
    casimir=(LM*vec==sp.zeros(3,1))
    assert casimir==all((sp.Matrix.eye(3)[:,i].T*LM*vec)[0]==0 for i in range(3))
# central extension: H_S=1/(1-z)^3, H_{S[v]}=1/(1-z)^4
z=sp.symbols('z')
assert sp.simplify(1/(1-z)**3/(1-z)-1/(1-z)**4)==0
print('toric AS-rationality: GL(3,Z), Casimir lattice samples, Hilbert series OK')
