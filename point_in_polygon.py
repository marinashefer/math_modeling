import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate

import shapely.geometry as geom 
phi = np.linspace(0,2*np.pi,40)
r = 0.5 + np.cos(phi)
x = r * np.cos(phi)
y = r * np.sin(phi)

spline_coords, figure_spline_part = interpolate.splprep([x,y], s = 0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color  = 'g', lw = 4)

curve_coords = []
for i in range (len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i],spline_curve[1][i] ])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 100
x_pictures_limits = [-0.5,2]
y_pictures_limits = [-1,1]

for x_point_coord in np.linspace (*x_pictures_limits,points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point (x_point_coord, y_point_coord)
        if p.within(polygon):
            plt.plot (x_point_coord, y_point_coord, 'ko', ms = 0.5)


plt.axis('equal')
plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('KILL7.png')