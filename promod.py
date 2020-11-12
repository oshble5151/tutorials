def ncmod(ncfile:str):
    global file,nml
    import netCDF4 as nc
    import numpy as np
    file = nc.Dataset(ncfile,'r')
    nml = file.variables.keys()
    print(file.variables.keys())
    for i in nml:
        globals()[i] = file.variables[i][:]
        if isinstance(globals()[i],np.ma.core.MaskedArray):
            globals()[i].mask=None
        
        else:
            pass 
ncmod('D:/test/au/ERA_tas/atmos_month2001_0025_n.nc')
print(globals())     
