# -*- coding: utf-8 -*-
"""
Models the charge density on a predefined grid
"""
def charge_density(x, y, charge, center, radius):
    rho = []
    for i in range(len(x)):    
        values = []    
        for j in range(len(x)):    
            if (x[i][j]-center[0])**2+(y[i][j]-center[1])**2<=radius**2:
                values.append(charge)
            elif (x[i][j]-center[2])**2+(y[i][j]-center[3])**2<=radius**2:
                values.append(-charge)
            else:
                values.append(0)
        rho.append(values)
    return rho