from sympy import *
L2, L3, a2, b, x_s, z_s, Lq3o = symbols('L2, L3, a2, b, x_s, z_s, Lq3o')

# L2  = 1280
# L3  = 1420
# x_s = 13.6
# z_s = 2

P  = Matrix([[x_s], [z_s]])
P1 = Matrix([[L2*cos(a2)],
                 [L2*sin(a2)]])
P2 = P1 + Matrix([[L3*cos(b)],
                  [L3*sin(b)]])

V1 = (P2-P1)
V2 = (P-P2)

s = sym.solveset((V1.T).dot(V2), b)
print(s)

# ConditionSet(b, Eq(-L2*L3*cos(a2 - b + da2) - L2*Lq3o*sin(a2 - b + da2) - L3**2 + L3*x_s*cos(b) + L3*z_s*sin(b) - Lq3o**2 - Lq3o*x_s*sin(b) + Lq3o*z_s*cos(b), 0), Reals)
[(3.14159265358979,), (-I*log(-0.001*(1420577.17885407*I*sqrt(-(-1000000.0*x_s**2*exp(I*a2) + 1280000000.0*x_s*exp(2.0*I*a2) + 1280000000.0*x_s - 1000000.0*z_s**2*exp(I*a2) - 1280000000.0*I*z_s*exp(2.0*I*a2) + 1280000000.0*I*z_s + 379639521081.0*exp(I*a2))*exp(I*a2)) - 2018039521081.0*exp(I*a2))/(x_s*(1420000.0 + 40491.0*I)*exp(I*a2) + z_s*(40491.0 - 1420000.0*I)*exp(I*a2) - 1817600000.0 - 51828480.0*I)),), (-I*log(0.001*(1420577.17885407*I*sqrt(-(-1000000.0*x_s**2*exp(I*a2) + 1280000000.0*x_s*exp(2.0*I*a2) + 1280000000.0*x_s - 1000000.0*z_s**2*exp(I*a2) - 1280000000.0*I*z_s*exp(2.0*I*a2) + 1280000000.0*I*z_s + 379639521081.0*exp(I*a2))*exp(I*a2)) + 2018039521081.0*exp(I*a2))/(x_s*(1420000.0 + 40491.0*I)*exp(I*a2) + z_s*(40491.0 - 1420000.0*I)*exp(I*a2) - 1817600000.0 - 51828480.0*I)),), (-I*log(-exp(I*a2)),)]
