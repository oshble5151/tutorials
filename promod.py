def ncmod(ncfile:str):
    global file,vkey,val,ncot,dkey,dim
    import netCDF4 as nc
    import numpy as np
    file = nc.Dataset(ncfile,'r')
    vkey = list(file.variables.keys())
    dkey =  list(file.dimensions.keys())
    
    print(file.variables.keys())
    for i in vkey:
        globals()[i] = file.variables[i][:]
        if isinstance(globals()[i],np.ma.core.MaskedArray):
            globals()[i].mask=None
        
        else:
            pass
    
    def dim():
        i = len(dkey)
        cot=[x for x in range(1,i+1)]
        ncot = [str(x)+'.'+y for x,y in zip(cot,dkey)];print(ncot)
        s=input('select num:')
        for i in ncot:
            if i.startswith(s)==True:
                return(file.dimensions[dkey[int(s)-1]])
        
        
    def val():
        i = len(vkey)
        cot=[x for x in range(1,i+1)]
        ncot = [str(x)+'.'+y for x,y in zip(cot,vkey)];print(ncot)
        s=input('select num:')
        for i in ncot:
            if i.startswith(s)==True:
                return(file.variables[vkey[int(s)-1]])
            
               
        
ncmod('D:/test/au/ERA_tas/atmos_month2001_0025_n.nc')



print(globals())     
