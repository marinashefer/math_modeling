import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

img = plt.imread('photo.jpeg')
fig, ax = plt.subplots()
ax.imshow(img)

x = [140,150,160,165,180,190,200,210,220,225,223,230,226,225,230,234,234,230,238,230,225,215,205,200,195,180,175,170,160,150,130,140]
y = [70,65,50,45,33,40,45,40,45,45,55,60,65,70,77,77,78,85,95,100,95,93,92,85,80,105,105,107,100,105,75,70]

spline_coords, figure_spline_part = interpolate.splprep([x,y], s = 0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color  = 'g', lw = 4)

curve_coords = []
for i in range (len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i],spline_curve[1][i] ])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 100
x_pictures_limits = [70,810]
y_pictures_limits = [1000,0]

for x_point_coord in np.linspace (*x_pictures_limits,points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point (x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot (x_point_coord, y_point_coord, 'ro', ms = 0.5)

plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('tuman.png')