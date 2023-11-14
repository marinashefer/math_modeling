import numpy as np
import lab_3_task_1 as ph

x0 = 8
y0 = 2
v0x = 10
g = 9.8
t = np.arange(0, 5, 0.01)

x = x0 + v0x * t
y = y0 + v0x * t - (g * t**2 / 2)