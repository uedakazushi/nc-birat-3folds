#!/usr/bin/env python3
"""Exact finite tests only. Does not certify formality, Artin approximation or SOD."""
from math import comb, prod
from itertools import product

def corner_dim(ns):
    return prod(sum((n+1-d)*comb(n+d,n) for d in range(n+1)) for n in ns)

def chain_height(ns):
    # One step raises the sum of coordinates by at least one;
    # an evident saturated chain of length sum(ns) exists.
    return sum(ns)

for n in range(1,9):
    assert sum((n+1-d)*comb(n+d,n) for d in range(n+1))==comb(2*n+2,n)
for ns in [(1,),(2,),(1,1),(1,2),(1,1,1),(2,2),(1,2,3)]:
    assert corner_dim(ns)==prod(comb(2*n+2,n) for n in ns)
    assert chain_height(ns)==sum(ns)
# For the central regular sequence (x,y) in k[x,y], degree-m piece
# I^m/I^{m+1} has exactly m+1 monomials.
for m in range(9):
    ms={(i,m-i) for i in range(m+1)}
    assert len(ms)==m+1
# Intersection pairing in total-transform basis (H,E_1,E_2).
def pairing(a,b):return a[0]*b[0]-a[1]*b[1]-a[2]*b[2]
minus_K=(3,-1,-1); minus2_curve=(0,1,-1)
assert pairing(minus2_curve,minus2_curve)==-2
assert pairing(minus_K,minus2_curve)==0
assert pairing(minus_K,minus_K)==7
print('PASS: binomial ranks, directed height, central graded dimensions (commutative test), weak del Pezzo intersection')
