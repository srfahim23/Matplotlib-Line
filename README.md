# Matplotlib-Line
# LineStyle
You can use the keyword argument linestyle, or shorter 1s, to change the style of the plotted line:

Example

Use a dotted line:

    import matplotlib.pyplot as plt
    import numpy as np

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, linestyle = 'dotted')
    plt.show()

Note:You can see the result in the top first picture graph    

Example

Use a dashed line:

    plt.plot(ypoints, linestyle = 'dashed')

Note: You can see the result in the second picture graph   

# Shorter Syntax
The line style can be written in a shorter syntax:

Linestyle can be written as 1s.

dotted can be written as :.

dashed can be written as --.

Example 

Shorter Syntax:

    plt.plot(ypoints, 1s = ':')

Note: You can see the result in the top third picture's    

