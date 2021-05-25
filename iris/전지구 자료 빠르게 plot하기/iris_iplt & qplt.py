import matplotlib.pyplot as plt

import iris
import iris.quickplot as qplt

## only 2dim
f = iris.load_cube('file_name')

iplt.contourf(f) # no color bar & name
qplt.contourf(f) # color bar & name

iplt.pcolormesh(f) 
qplt.pcolormesh(f)

# applying cmap
import matplotlib.cm as mpl_cm
cmap = mpl_cm.get_cmap('brewer_OrRd_09')

qplt.contourf(temperature_cube, brewer_cmap.N, cmap=brewer_cmap)
qplt.pcolormesh(temperature_cube, cmap=brewer_cmap)

# ciation
qplt.contourf(temperature_cube, brewer_cmap.N, cmap=brewer_cmap)
iplt.citation('ciation')

plt.gca().coastlines()
