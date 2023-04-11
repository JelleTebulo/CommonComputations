# from scipy.spatial.transform import Rotation as R
# import numpy as np
import sympy as sym
L2, L3, a2, da2, b, x_s, z_s = sym.symbols('L2, L3, a2, da2, b, x_s, z_s')
L2 = 6
L3 = 4
P  = sym.Matrix([[x_s], [z_s]])
P1 = sym.Matrix([[L2*sym.cos(a2+da2)],
                 [L2*sym.sin(a2+da2)]])
P2 = P1 +sym.Matrix([[L3*sym.cos(b)],
                     [L3*sym.sin(b)]])

V1 = P2-P1

V2 = P-P2

s = sym.solve(V1.T.dot(V2), b)
print(f's ={s}')