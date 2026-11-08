"""Exact ideals of the marked reducible-cubic extension fibers over Q.

Run beside verify_fixed_dp8.py. Its 12 coefficients are the Jacobi equations
in the full 6-dimensional space of linear lifts, before taking radicals.
"""
import sympy as s
import verify_fixed_dp8 as base

v,w = base.v,base.w
a,b,c,d,e,f = gvars = tuple(base.pars[9:])  # x0,x1,y0,y1,z0,z1
cubics = (v,-w,v**2,-v*w,-w**2,v**3,-v**2*w,-v*w**2,w**3)

# Each record gives the affine cubic (homogenize to degree 3) and generators
# of its claimed scheme ideal, in the same fiber coordinates as the paper.
cases = [
    ('secant-line', v*(1+v**2+w**2), [a,b,c,d,e,f+1]),
    ('secant-conic', v+w+v*w, [a,b-1,c,d,e,f]),
    ('secant-both', v*(w+v**2+w**2), [a,b+f,2*c+f-1,d,e,f**2-1]),
    ('tangent-line', v*(v+(w+1)**2), [a,b-2,c-2,d,e,f+1]),
    ('tangent-conic', (v-1)*(v+w**2+2*w), [a-1,b+2,c,d+1,e,f-1]),
    ('tangent-both', v*(v+w**2), [2*a-f-1,b,c,d,e,f**2-1]),
    ('triangle-side', v*(1+w)*(1+v), [a+e-1,b-1,c-e,d,f]),
    ('triangle-vertex', v*w*(1+v+w), [a,b+f,c-e,d,e*(f+1)]),
    ('concurrent-side', v*(v+w-1)*(w-1), [a-e+1,b+2,c+2,d,f+1]),
    ('concurrent-center', v*w*(v+w), [a,b,c,d]),
    ('double-line', v**2*(1+w), [a+e-1,b+f,c+f,d,f**2]),
    ('single-line', v*(1+w)**2, [a+e,b-2,d,f+1]),
    ('double-vertex', v**2*w, [a,b*e,c,d]),
    ('triple-line', v**3, [a*f-2*c*e,b-2*c,c**2,c*f,d]),
]

for label,P,target in cases:
    poly = s.Poly(P,v,w)
    coordinates = []
    for signed_monomial in cubics:
        sign,monomial = signed_monomial.as_coeff_Mul()
        coordinates.append(sign*poly.coeff_monomial(monomial))
    assert s.expand(P - sum(t*q for t,q in zip(coordinates,cubics))) == 0
    values = dict(zip(base.pars[:9],coordinates))
    equations = [e.subs(values) for e in base.cs.values()]
    def basis(generators):
        return list(s.groebner(generators,*gvars,order="lex",domain=s.QQ))
    assert basis(equations) == basis(target), label
    print(label, 'OK')
