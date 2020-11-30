import os
os.chdir('package path')
import netCDF4 as nc
import numpy as np
import matplotlib.pyplot as plt
from matplotlib import docstring
from matplotlib.pyplot import gcf,Axes,sci,cbook

def gca(**kwargs):
       return gcf().gca(**kwargs)
       
## plt.imshow Source code (X=>self)
@docstring.copy(Axes.imshow)
def imshow(self,
    cmap='jet',
    norm=None,
    aspect=None,
    interpolation=None,
    alpha=None,
    vmin=None,
    vmax=None,
    origin=None,
    extent=None,
    shape=cbook.deprecation._deprecated_parameter,
    filternorm=1,
    filterrad=4.0,
    imlim=cbook.deprecation._deprecated_parameter,
    resample=None,
    url=None,
    *,
    data=None,
    **kwargs):
       __ret = gca().imshow(
        self, cmap=cmap, norm=norm, aspect=aspect,
        interpolation=interpolation, alpha=alpha, vmin=vmin,
        vmax=vmax, origin=origin, extent=extent, shape=shape,
        filternorm=filternorm, filterrad=filterrad, imlim=imlim,
        resample=resample, url=url, **({"data": data} if data is not
        None else {}), **kwargs)
       sci(__ret)
       plt.gca().invert_yaxis()
       plt.show()

       


       
