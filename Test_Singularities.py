from numpy import *
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt

L2   = 1280
L3   = 1419.996
x    = 1230+1155
y    = 1200+500
y_so = 203
z    = 100
x_s  = float(sqrt(x**2+y**2-y_so**2)-320)
x_s  = 2921.803-320
x_s  = linspace(0,3000,10000)
z_s  = z-780
z = linspace(-1000,2000,13)
z_s_linspace = z-780
# b    = linspace(deg2rad(-40), deg2rad(40), 100)
b    = deg2rad(10)

fig, ax = plt.subplots()

for z_s in z_s_linspace:
    a2 = - 2*arctan((2*L2*tan(b/2) + sqrt(2)*sqrt(-(-2*L2**2 + 2*L3**2 - 4*L3*x_s*cos(b) - 4*L3*z_s*sin(b) + x_s**2*cos(2*b) + x_s**2 + 2*x_s*z_s*sin(2*b) - z_s**2*cos(2*b) + z_s**2)/(cos(b) + 1)**2))/(L2*tan(b/2)**2 - L2 + L3*tan(b/2)**2 + L3 + x_s*tan(b/2)**2 - x_s - 2*z_s*tan(b/2)))
    a2 = rad2deg(a2)
    j2 = 90 - a2
    x_s = x_s[~isnan(j2)]
    j2 = j2[~isnan(j2)]

    ax.plot(x_s+320, j2, linewidth=4, label=f'z = {int(z_s)+780}')

ax.set_xlabel(r'$\sqrt{x^2+y^2} [mm]$', fontsize=20)
ax.set_ylabel(r'$j_2 [^\circ]$', fontsize=20)
ax.grid(True)
ax.legend()
ax.set_ylim([-90, 90])
ax.set_title(r'Mogelijke posities met $\beta=10^\circ$', fontsize=20)
plt.xticks(fontsize=20)
plt.yticks(fontsize=20)



# fig, ax = plt.subplots()
# ax.plot(rad2deg(b), j2)
# ax.set_xlabel(r'$beta$')
# ax.set_ylabel(r'$j_2$')
# ax.grid(True)
# plt.show()



