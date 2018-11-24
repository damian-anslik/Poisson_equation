# -*- coding: utf-8 -*-
"""
Sets up the grid environment
"""
def grid(x_range, y_range, num_vertices):
    import numpy as np    
    '''Set up the x, y grid'''
    x_min, x_max = x_range[0], x_range[1]
    y_min, y_max = y_range[0], y_range[1]
    step_width_x = (abs(x_min)+x_max)/num_vertices
    step_width_y = (abs(y_min)+y_max)/num_vertices
    
    x = [[i for i in np.arange(x_min, x_max, step_width_x)] for i in range(num_vertices)]
    y = [[i]*num_vertices for i in np.arange(y_min, y_max, step_width_y)]
    return [x, y]

