import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

img = plt.imread('horsehead.jfif')
fig, ax = plt.subplots()
ax.imshow(img)
x = [250, 340, 350, 150, 80, 60, 100, 180, 250, 300, 450, 500, 550, 630, 682, 692, 660, 250]
y = [800, 620, 400, 500, 480, 400, 300, 260, 100, 110, 130, 126, 124, 200, 300, 600, 800, 800]

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color='g', lw=4)

plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('KILL6.png')