# from scipy.spatial.transform import Rotation as R
import numpy as np
import sympy as sym
L2, L3, a2, b, x_s, z_s, Lq3o = sym.symbols('L2, L3, a2, b, x_s, z_s, Lq3o')

# L2  = 1280
# L3  = 1420
# x_s = 13.6
# z_s = 2
# Lq3o = 40.491

P  = sym.Matrix([[x_s], [z_s]])
P1 = sym.Matrix([[L2*sym.cos(a2)],
                 [L2*sym.sin(a2)]])
P2 = P1 + sym.Matrix([[L3*sym.cos(b) - Lq3o*sym.sin(b)],
                      [L3*sym.sin(b) + Lq3o*sym.cos(b)]])

V1 = (P2-P1)
V2 = (P-P2)

s = sym.solveset((V1.T).dot(V2), b)
print(s)

# ConditionSet(b, Eq(-L2*L3*cos(a2 - b + da2) - L2*Lq3o*sin(a2 - b + da2) - L3**2 + L3*x_s*cos(b) + L3*z_s*sin(b) - Lq3o**2 - Lq3o*x_s*sin(b) + Lq3o*z_s*cos(b), 0), Reals)

