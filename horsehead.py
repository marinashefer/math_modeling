import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('horsehead.jfif')
fig, ax = plt.subplots()
ax.imshow(img)
x = [250, 340, 350, 150, 80, 60, 100, 180, 250, 300, 450, 500, 550, 630, 682, 692, 660, 250]
y = [800, 620, 400, 500, 480, 400, 300, 260, 100, 110, 130, 126, 124, 200, 300, 600, 800, 800]

spline_coords, figure_spline_part = interpolate.splprep([x, y], s=0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color='k', lw=4)

curve_coords = []
for i in range(len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i], spline_curve[1][i]])

polygon = geom.Polygon(curve_coords)
points_numbr_per_side = 100
x_pictures_limits = [50, 800]
y_pictures_limits = [800, 0]

for x_point_coord in np.linspace(*x_pictures_limits, points_numbr_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_numbr_per_side):
        p = geom.Point(x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot(x_point_coord, y_point_coord, 'ko', ms=0.5)

plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('KILL8.png')