#!/usr/bin/env python

__author__ = "Daniel del Castillo"
__version__ = "0.0.0"

import numpy as np
from mpl_toolkits.mplot3d import Axes3D

from wrapyplot import wrapyplot

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 1a) Multiple plots
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
wpp = wrapyplot(num='Hey',dpi=120)
ax1 = wpp.add_ax(411,3,xlim=(-10,10),ylim=(-1,10),title='aloha')
ax2 = wpp.add_ax(412,title='heya')
ax3 = wpp.add_ax(155,polar=True)
ax4 = wpp.add_ax(426)
wpp.figure.set_size_inches(20,10,forward=True)

# 1b) Dynamic plotting

ax1.plot([],[],c='k')
wpp.pre_anim()
xdata = []; ydata = []
for x in np.arange(0,10,0.5):
    xdata.append(x)
    ydata.append(np.exp(-x**2)+10*np.exp(-(x-7)**2))
    ax1.lines[0].set_xdata(xdata); ax1.lines[0].set_ydata(ydata)
    wpp.update_fig()

# wpp.show() # does not make any difference

# <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
# 3) 3D Plot
# >>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ff_3D = wrapyplot()
ax1_3D = ff_3D.add_ax(211,5,projection='3d')
ax2_3D = ff_3D.add_ax(212,xlim=(0,200),ylim=(0,1))

ff_3D.show_all()
