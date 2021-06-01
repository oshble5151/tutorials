## 30년 동안의 1월 자료의 평균값에 대한 anomoly

30년 동안의 1월 자료의 평균값에 대한 anomoly를 구해보려 한다.
```python
import iris
from iris.experimental.equalise_cubes import equalise_attributes
import iris.quickplot as qplt
import matplotlib.pyplot as plt
from iris.std_names import STD_NAMES

li = ['atmos_month_%d.nc'%i for i in range(1981,2011)]
month_1 = iris.Constraint(time = lambda cell: cell.point.month ==1)

 for i,j in enumerate(li):
      print(j)
      exec("file%d = iris.load_cube(j,'tas'&month_1)"%(i+1))
 
 cube_list = iris.cube.CubeList([])
 
 for i in range(len(li)):
      exec('cube_list.append(file%d)'%(i+1))
 
      #print(cube_list)
 
 equalise_attributes(cube_list)
 
 month1_30year_file = cube_list.merge_cube()
 print(month1_30year_file)
 26
 27 month1_30year_collap_time = month1_30year_file.collapsed('time',iris.analysis.MEAN)
 28
 29 anomoly_month1_30year = month1_30year_file - month1_30year_collap_time
 30
 31 print(anomoly_month1_30year)
 32
 33 STD_NAMES['temp_anolmary'] = {'canonical_units': 'K'}
 34 #anomoly_month1_30year.standard_name = 'surface_temperature_anomaly'
 35 anomoly_month1_30year.standard_name = 'temp_anolmary'
 36
 37 iris.save(anomoly_month1_30year,'anomoly_30year.nc')
 38
 39 time_slice = anomoly_month1_30year.slices(['latitude', 'longitude'])
 40
 41 for_index_list = [list(time_slice),[x for x in range(30)]]
 42 print(list(time_slice))
 43
 44 for i,j in zip(*for_index_list):
 45     plt.subplot(5,6,j+1)
 46     qplt.pcolormesh(i)
 47     #iplt.citatiion(' lat:'+z+' degrees_N'+'\n time: 1981_01_16')
 48 plt.show()

 
equalise_attributes(cube_list)

month1_30year_file = cube_list.merge_cube()

month1_30year_collap_time = month1_30year_file.collapsed('time',iris.analysis.MEAN)

anomoly_month1_30year = month1_30year_file - month1_30year_collap_time
```
![image](https://user-images.githubusercontent.com/73323188/120260463-ea034100-c2d0-11eb-9ad4-9f5ebc433e18.png)
