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

# Line Style
You can choose any of these styles:

    Style                   Or

    'solid' (default)       '-'

    'dotted'                ':'

    'dashed'                '--'

    'dashdot'               '-.'

    'None'                  "or''


# Line Color
You can us the keyword argument color or the shorter c to set the color of the line:

Example

SEt the line color to red:

    import matplotlib.pyplot as plt
    import numpy as np

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, color = 'r')
    plt.show()

Note: You can see the result in the top fourth's picture


You can also use Hexadecimal color value:

Example 

Plot with a beatiful gree line;

    '''plt.plot(ypoints, c = '#4CAF50')
    '''

Note: You can see the result in the top five's picture graph

Or any of the 140 supported color names.

Example 

Plot with the color named "hotpink":

    '''
    plt.plot(ypoints, c = 'hotpink')
    '''

Note: You can see the result in the top six's picture graph

# Line Width 
You can use the keyword argument linewidth or the shorter lw to change the width of the line.

The value is floating number, in points:

Example 

Plot with a 20.5pt wide line:

    import matplotlib.pyplot as plt
    import numpy as np

    ypoints = np.array([3, 8, 1, 10])

    plt.plot(ypoints, linewidth = '20.5')
    plt.show()

Note: You can see the result in the top seven's no. picture graph

# Multiple Lines
You can plot as many lines as you like by simply adding more plt.plot() functions:

Example 

Draw two lnes by spcifying a plt.plot() function for each line:

    import matplotlib.pyplot as plt
    import numpy as np

    y1 = np.array([3, 8, 1, 10])
    y2 = np.array([6, 2, 7, 11])

    plt.plot(y1)
    plt.plot(y2)

    plt.show()

Note: You can see the result in the top eight's no. picture graph

You can also plot many lines by adding the points for the x- and y-axis for each line in the same plt.plot() function.

(In the example above we only specified the points on th ey-axis, meaning tha t the points on the x-axis got the default values (0, 1, 2, 2).)

The x- and y- values come in pairs:

Example

Draw tow lines by specifying the x- and y-point values for both line:

    import matplotlib.pyplot as plt
    import numpy as np

    x1 = np.array([0, 1, 2, 3])
    y1 = np.array([3, 8, 1, 10])

    x2 = np.array([0, 1, 2, 3])
    y2 = np.array([6, 2, 7, 11])

    plt.plot(x1, y1, x2, y2)
    plt.show()

Note: You can see the result in the added top nine's no. picture graph



