import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
from matplotlib.patches import Ellipse

# NUM = 250
#
# ells = [Ellipse(xy=rnd.rand(2)*10, width=rnd.rand(), height=rnd.rand(), angle=rnd.rand()*360)
#         for i in range(NUM)]
#
# fig = plt.figure(0)
# ax = fig.add_subplot(111, aspect='equal')
# for e in ells:
#     ax.add_artist(e)
#     e.set_clip_box(ax.bbox)
#     e.set_alpha(rnd.rand())
#     e.set_facecolor(rnd.rand(3))
#
# ax.set_xlim(0, 10)
# ax.set_ylim(0, 10)
#
# plt.show()





# define the matrix
A = np.array([[1.0,1.0], [0.0, 1.0]])
R = np.array([[0.25,0.5], [0.5, 1]])
print("Matrix A:")
print(A)
print("\nMatrix R:")
print(R)

sigma_bar = np.zeros([2,2,6])
eig_vec = np.zeros([2,1,6])
eig_val = np.zeros([2,2,6])

fig1 = plt.figure(0, figsize=(5,8))
subplot_ = [321, 322, 323, 324, 325, 326]
for i in range(6):
    if i == 0:
        1;
    else:
        sigma_bar[:,:,i] = np.dot( np.dot(A, sigma_bar[:,:,i-1]), A.transpose()) + R
    print("\nsigma_bar: " + str(i))
    print(sigma_bar[:,:,i])
    eig_val[:,:,i] = np.linalg.eig(sigma_bar[:,:,i])[1]
    angle_cal = np.arctan(np.linalg.eig(sigma_bar[:,:,i])[1][1,0] / np.linalg.eig(sigma_bar[:,:,i])[1][0,0] )

    ax = fig1.add_subplot(subplot_[i], aspect='equal')
    ells = Ellipse(xy=(0,0),
    width = np.linalg.eig(sigma_bar[:,:,i])[0][0],
    height = np.linalg.eig(sigma_bar[:,:,i])[0][1],
    angle = angle_cal * 180.0 / np.pi,
    edgecolor  = 'black',
    facecolor='red')
    ax.add_patch(ells)
    m = 5
    n = 2
    if(i == 0):
        ax.set_xlim(-m * 0.2, m * 0.2)
        ax.set_ylim(-m * 0.2 / n, m * 0.2 / n)
    else:
        ax.set_xlim(-m * i, m * i)
        ax.set_ylim(-m * i / n, m * i / n)
    ax.title.set_text('t = ' + str(i))
    ax.grid()
# plt.show()
plt.savefig('../figures/ch3p1.png', bbox_inches='tight')






















 ##
