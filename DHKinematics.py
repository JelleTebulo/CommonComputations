import numpy as np
import sympy as sym

def Compute_H(i):
    H = sym.Matrix([[sym.cos(DHt[i, 0]) , -sym.sin(DHt[i, 0])*sym.cos(DHt[i, 1]) , sym.sin(DHt[i, 0])*sym.sin(DHt[i, 1])  , DHt[i, 2]*sym.cos(DHt[i, 0])],
                    [sym.sin(DHt[i, 0])   , sym.cos(DHt[i, 0])*sym.cos(DHt[i, 1])  , -sym.cos(DHt[i, 0])*sym.sin(DHt[i, 1]) , DHt[i, 2]*sym.sin(DHt[i, 0])],
                    [0                    , sym.sin(DHt[i, 1])                     , sym.cos(DHt[i, 1])                     , DHt[i, 3]],
                    [0                    , 0                                      , 0                                      , 1]])
    return H

th_2 = sym.symbols('th_2')
# th is the angle from x(n-1) to x(n) around z(n-1)
# alpha is the angle from z(n-1) to z(n) around x(n)
# r or a is the distance between the origin of the n-1 frame and the origin of the n frame along the x(n) direction
# d is the distance from x(n-1) to x(n) along the z(n-1) direction.


# Link lengths in centimeters
a1 = 1  # Length of link 1
a2 = 1  # Length of link 2
a3 = 1  # Length of link 3
a4 = 1  # Length of link 4
a5 = 1  # Length of link 5
a6 = 1  # Length of link 6

# Initialize values for the displacements
d1 = 1  # Displacement of link 1

# Initialize values for the joint angles (degrees)
th_1 = 0  # Joint 1
th_2 = th_2  # Joint 2
th_3 = 0  # Joint 3
th_4 = 0  # Joint 4
th_5 = 0  # Joint 5
th_6 = 0  # Joint 5

# Declare the Denavit-Hartenberg table.
# It will have four columns, to represent:
# th, alpha, r, and d
# We have the convert angles to radians.
DHt = sym.Array([[np.deg2rad(th_1)    , np.deg2rad(-90), a2 , a1],
                [np.deg2rad(-90) + th_2 , np.deg2rad(180), a3 , 0],
                [np.deg2rad(th_3+180), np.deg2rad(90) , -a4, 0],
                [np.deg2rad(th_4)    , np.deg2rad(-90), 0  , -a5],
                [np.deg2rad(th_5)    , np.deg2rad(90) , 0  , 0],
                [np.deg2rad(th_6+180), np.deg2rad(180), 0  , -a6]])


H1_0 = Compute_H(0)  # Homogeneous transformation matrix from frame 0 to frame 1
H2_1 = Compute_H(1)  # Homogeneous transformation matrix from frame 1 to frame 2
H3_2 = Compute_H(2)  # Homogeneous transformation matrix from frame 2 to frame 3
H3_0 = H1_0*H2_1*H3_2

