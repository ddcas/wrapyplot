#!/usr/bin/env python

__author__ = "Daniel del Castillo"
__version__ = "0.0.0"

"""

wrapyplot.py:
main class of wrapyplot, a very thin wrapper for matplotlib.pyplot
allowing easy dynamic plot generation


next:
+ MatplotlibDeprecationWarning 
+ consider FuncAnimation instead of current blitting method

"""


# necessary imports
import matplotlib.pyplot as plt
import matplotlib.gridspec as gridspec

class wrapyplot():

    def __init__(self,**kwargs):
        self.rows = 0
        self.cols = 0
        self.axes = []
        self.hrs = []
        # interactive mode off
        plt.ioff()
        self.figure = plt.figure(**kwargs,facecolor='white')

    def add_ax(self,pos=111,hr=1,**kwargs):
        nr, nc, num = list(map(int,str(pos)))
        # if the list of axes is empty
        if not self.axes: self.rows, self.cols = nr, nc
        # if we need to reshape the subplot grid
        if num > self.rows*self.cols:
            for i,ax in enumerate(self.axes,start=1):
                ax.change_geometry(nr,nc,i)
            self.rows = nr; self.cols = nc
        # add height ratio to the list
        self.hrs.append(hr)
        gs = gridspec.GridSpec(self.rows,self.cols,
                height_ratios=self.hrs+[1]*(self.rows*self.cols-len(self.hrs)))
        self.axes.append(plt.subplot(gs[len(self.hrs)-1],**kwargs))

        return self.axes[-1]

    def pre_anim(self): # This function should be embedded or "hidden"
        self.figure.tight_layout()
        # the first draw comes before the animated plots
        self.figure.canvas.draw()
        # capture the background of the figure
        self.backgrounds = [self.figure.canvas.copy_from_bbox(ax.bbox) for ax in self.axes]

    def update_fig(self):
        for ax,bg in zip(self.axes,self.backgrounds):
            self.figure.canvas.restore_region(bg)
            for line in ax.lines:
                ax.draw_artist(line)
            self.figure.canvas.blit(ax.bbox)
        plt.pause(0.000000000001)

    def show(self):
        self.figure.show()

    def show_all(self):
        plt.show()
