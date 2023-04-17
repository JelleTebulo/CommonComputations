from sympy import *
L2, L3, a2, b, x_s, z_s = symbols('L2, L3, a2, b, x_s, z_s')

# P  = Matrix([[x_s], [z_s]])
# P1 = Matrix([[L2*cos(a2)],
#                  [L2*sin(a2)]])
# P2 = P1 + Matrix([[L3*cos(b) ],
#                   [L3*sin(b)]])
#
# V1 = (P2-P1)
# V2 = (P-P2)

# s = solve((V1.T).dot(V2), b)

# s[0] =-da2 - 2*atan((2*L2*tan(b/2) - sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))
# s[1] =-da2 - 2*atan((2*L2*tan(b/2) + sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))

eq = - 2*atan((2*L2*tan(b/2) + sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))

eq_subs = eq.subs({L2:1280, L3:1420})
eq_subs = -2*atan((sqrt(2)*sqrt((-x_s**2*cos(2*b) - x_s**2 - 2*x_s*z_s*sin(2*b) + 5680*x_s*cos(b) + z_s**2*cos(2*b) - z_s**2 + 5680*z_s*sin(b) - 756000)/(cos(b) + 1)**2) + 2560*tan(b/2))/(x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2) + 2700*tan(b/2)**2 + 140))
