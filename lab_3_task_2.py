import numpy as np
import lab_3_task_1 as ph

h = 100
a = 3.1415926535 / 3
b = 30
g = ph.acceleration_of_gravity

v = np.sqrt(g * h *  np.tan(b)**2 / 2 * np.cos(a)**2 * (1 - np.tan(b)) * np.tan(a))
print(v)