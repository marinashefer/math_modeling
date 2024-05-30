import matplotlib.pyplot as plt
import numpy as np
from scipy import interpolate
import shapely.geometry as geom

# img = plt.imread('photo.jpeg')
fig, ax = plt.subplots()
# ax.imshow(img)

x = [140,150,160,165,180,190,200,210,220,225,223,230,226,225,230,234,234,230,238,230,225,215,205,200,195,180,175,170,160,150,130,140]
y = [70,65,50,45,33,40,45,40,45,45,55,60,65,70,77,77,78,85,95,100,95,93,92,85,80,105,105,107,100,105,75,70]

spline_coords, figure_spline_part = interpolate.splprep([x,y], s = 0)
spline_curve = interpolate.splev(figure_spline_part, spline_coords)
plt.plot(spline_curve[0], spline_curve[1], color  = 'g', lw = 4)

curve_coords = []
for i in range (len(spline_curve[0])):
    curve_coords.append([spline_curve[0][i],spline_curve[1][i] ])

polygon = geom.Polygon(curve_coords)
points_number_per_side = 500
x_pictures_limits = [70,810]
y_pictures_limits = [1000,0]

points_coords = []

for x_point_coord in np.linspace (*x_pictures_limits,points_number_per_side):
    for y_point_coord in np.linspace(*y_pictures_limits, points_number_per_side):
        p = geom.Point (x_point_coord, y_point_coord)
        if p.within(polygon):
            # plt.plot (x_point_coord, y_point_coord, 'ro', ms = 0.5)
            points_coords.append(x_point_coord)
            points_coords.append(y_point_coord)

x_p = np.array(points_coords[0::2])
y_p = np.array(points_coords[1::2])

def bell_function(x, y, intensity=1, dec_rate=[0.5, 0.5]):
    scalar_func = intensity * np.exp(- dec_rate[0]*x**2 - dec_rate[1]*y**2) 
    return scalar_func

intensity_centerums_x = [70, 140, 200, 50]
intensity_centerums_y = [70, 90, 120, 100]
intensity_values = [0.3, 0, 1, 0.04]

def scalar_function(x, y, int_cen_x, int_cen_y, int_vel):
    scalar_field = 0.0
    for i in range(0, len(int_cen_x)):
        scalar_field += int_vel[i] * bell_function(x-int_cen_x[i], y-int_cen_y[i], 0.005, [0.0005, 0.0005])
    return scalar_field

scalar_fields = []
for i in range(0, len(x_p)):
    calculate = scalar_function(x_p[i], y_p[i], intensity_centerums_x, 
                                intensity_centerums_y, intensity_values)
    scalar_fields.append(calculate)


sc_plot = ax.scatter(x_p, y_p, c=scalar_fields)
cbar = fig.colorbar(sc_plot)
cbar.set_label("Комбинированное скалярное поле:")

x,y = np.meshgrid(np.linspace(168, 180, 3), np.linspace(100,80,1))
u = -1
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(173, 185, 3), np.linspace(93,90,1))
u = -1.5
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(179, 190, 3), np.linspace(87,80,1))
u = -3
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(179, 190, 3), np.linspace(83,80,1))
u = -4
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(184, 193, 3), np.linspace(80,80,1))
u = -1.5
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(187, 196, 3), np.linspace(77,75,1))
u = -0.1
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(197, 209, 3), np.linspace(80,75,1))
u = 1
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(200, 211, 3), np.linspace(83,75,1))
u = 2
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(203, 213, 3), np.linspace(86,75,1))
u = 1.4
v = -1
plt.quiver(x,y,u,v)

x,y = np.meshgrid(np.linspace(205, 215, 3), np.linspace(89.5,75,1))
u = 1
v = -1
plt.quiver(x,y,u,v)


plt.plot(x,y,lw = 2, color = 'w')
plt.ylim()
plt.savefig('tuman2.png')