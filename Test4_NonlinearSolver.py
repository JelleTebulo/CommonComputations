import numpy as np
from sympy import *
L2, L3, a2, b, x_s, z_s, Lq3o = symbols('L2, L3, a2, b, x_s, z_s, Lq3o')

L2 = 1280
L3 = 1420
Lq3o = 40.491

P = Matrix([[x_s], [z_s]])
P1 = Matrix([[L2*cos(a2)],
                 [L2*sin(a2)]])
P2 = P1 + Matrix([[L3*cos(b) - Lq3o*sin(b)],
                 [L3*sin(b) + Lq3o*cos(b)]])

V1 = (P2-P1)
V2 = (P-P2)
eq = (V1.T).dot(V2)
# s = nonlinsolve([eq], b)
s = solve([-40.491*x_s*sin(b) + 1420.0*x_s*cos(b) + 1420.0*z_s*sin(b) + 40.491*z_s*cos(b) - 51828.48*sin(a2 - b) - 1817600.0*cos(a2 - b) - 2018039.521081], b)
print(s)

# {(ConditionSet(b, Eq(-40.491*x_s*sin(b) + 1420.0*x_s*cos(b) + 1420.0*z_s*sin(b) + 40.491*z_s*cos(b) - 51828.48*sin(a2 - b + da2) - 1817600.0*cos(a2 - b + da2) - 2018039.521081, 0), Reals),)}

