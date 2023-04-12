# from scipy.spatial.transform import Rotation as R
import numpy as np
import sympy as sym
L2, L3, a2, da2, b, x_s, z_s, Lq3o = sym.symbols('L2, L3, a2, da2, b, x_s, z_s, Lq3o')

# L2  = 1280
# L3  = 1420
# L2  = 10
# L3  = 5
# da2 = np.deg2rad(30.5)
# b   = np.deg2rad(27)
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

s = sym.solve((V1.T).dot(V2), b)


for i in range(len(s)):
    # print(f's ={sym.simplify(s[i])} rad')
    print(f's ={np.rad2deg(float(s[i]))} degrees')

for i in range(len(s)):
    print(f's[{i}] ={sym.simplify(s[i])}')
# a2[0] =-da2 - 2*atan((2*L2*tan(b/2) - sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))
# a2[1] =-da2 - 2*atan((2*L2*tan(b/2) + sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))

