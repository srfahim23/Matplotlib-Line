# Matplotlib Line
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linestyle = 'dotted')
# plt.show()


# This will be color red 
# import matplotlib.pyplot as plt
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, color = 'r')

# plt.show()

# Plot with a 20.5pt wide line:
# import matplotlib.pyplot as plt 
# import numpy as np

# ypoints = np.array([3, 8, 1, 10])

# plt.plot(ypoints, linewidth = '20.5')
# plt.show()

# Draw tow lines by specifying a plt.plot() function for each line:
# import matplotlib.pyplot as plt
# import numpy as np

# y1 = np.array([3, 8, 1, 10])
# y2 = np.array([6, 2, 7, 11])

# plt.plot(y1)
# plt.plot(y2)

# plt.show()

#Draw two lines by specifying the x- and y- point values for both lines:
import matplotlib.pyplot as plt
import numpy as np

x1 = np.array([0, 1, 2, 3])
y1 = np.array([3, 8, 1, 10])
x2 = np.array([0, 1, 2, 3])
y2 = np.array([6, 2, 7, 11])

plt.plot(x1, y1, x2, y2)
plt.show()