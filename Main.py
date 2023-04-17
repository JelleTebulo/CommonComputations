# from scipy.spatial.transform import Rotation as R
import numpy as np
from sympy import *
L2, L3, a2, b, x_s, z_s, Lq3o = symbols('L2, L3, a2, b, x_s, z_s, Lq3o')

L2   = 1280
L3   = 1419.996
x    = 1230+1155
y    = 1200+500
y_so = 203
z    = 0
x_s  = float(sqrt(x**2+y**2-y_so**2)-320)
z_s  = z-780

P  = Matrix([[x_s], [z_s]])
P1 = Matrix([[L2*cos(a2)],
                 [L2*sin(a2)]])
P2 = P1 + Matrix([[L3*cos(b)],
                      [L3*sin(b)]])

V1 = (P2-P1)
V2 = (P-P2)

s = solve((V1.T).dot(V2), b)


for i in range(len(s)):
    # print(f's ={sym.simplify(s[i])} rad')
    print(f's ={np.rad2deg(float(s[i]))} degrees')

for i in range(len(s)):
    print(f's[{i}] ={simplify(s[i])}')
# a2[0] = - 2*atan((2*L2*tan(b/2) - sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))
# a2[1] = - 2*atan((2*L2*tan(b/2) + sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))

