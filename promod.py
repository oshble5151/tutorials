import os ; os.chdir('C:/Users/eunky/Desktop')
def ncmod(ncfile:str):
    global file,nml
    import netCDF4 as nc
    import numpy as np
    file = nc.Dataset(ncfile,'r')
    nml = file.variables.keys()
    print(file.variables.keys())
    for i in nml:
        globals()[i] = file.variables[i][:]
        try:
            globals()[i].mask=None
        except:
            pass  
     
