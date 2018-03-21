# -*- coding: utf-8 -*-
"""
Created on Tue Mar 13 22:42:50 2018

@author: orpha
"""
import numpy as np
import matplotlib.pyplot as plt
import datetime


# =============================================================================
# x = np.arange(0, 5, 0.1);
x = np.arange(datetime.datetime(2018,1,1), datetime.datetime.now(), datetime.timedelta(7));
# =============================================================================
y = [i for i in range(11)]
plt.plot(x, y)
