import os ; os.chdir('./')
def nctest(file:str):
    import netCDF4 as nc
    import numpy as np
    nf = nc.Dataset(file,'r')
    nml = nf.variables.keys()
    print(nml)
    for i in nml:
        globals()[i] = nf.variables[i][:]


nctest('atmos_month2001_0025_n.nc')
print(tas)
