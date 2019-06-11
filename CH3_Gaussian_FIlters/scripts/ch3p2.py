import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib.patches import Ellipse


# define the matrix
sigma_bar_5 = np.array([
[41.25, 12.5],
[12.5 , 5.0 ]
])

sigma_5 = np.array([
[8.05, 2.44],
[2.44 , 1.95 ]
])
print("\nsigma_bar_5: ")
print(sigma_bar_5)
print("\nsigma_5: ")
print(sigma_5)

fig1 = plt.figure(0, figsize=(8,5))

# plot of sigma_bar
angle_cal_bar = np.arctan(np.linalg.eig(sigma_bar_5)[1][1,0] / np.linalg.eig(sigma_bar_5)[1][0,0] )

ax = fig1.add_subplot(aspect='equal')
ells_bar = Ellipse(xy=(0,0),
width = np.linalg.eig(sigma_bar_5)[0][0],
height = np.linalg.eig(sigma_bar_5)[0][1],
angle = angle_cal_bar * 180.0 / np.pi,
edgecolor  = 'black',
facecolor='gray')
ax.add_patch(ells_bar)

# plot of sigma
angle_cal = np.arctan(np.linalg.eig(sigma_5)[1][1,0] / np.linalg.eig(sigma_5)[1][0,0] )

ells = Ellipse(xy=(0,0),
width = np.linalg.eig(sigma_5)[0][0],
height = np.linalg.eig(sigma_5)[0][1],
angle = angle_cal * 180.0 / np.pi,
edgecolor  = 'black',
facecolor='red')
ax.add_patch(ells)



# formating of the plot
m = 5
n = 2
i = 5
ax.set_xlim(-m * i, m * i)
ax.set_ylim(-m * i / n, m * i / n)
ax.title.set_text('t = ' + str(i))
ax.grid()
# plt.show()
plt.savefig('../figures/ch3p2.png', bbox_inches='tight')






















 ##
