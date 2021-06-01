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
 equalise_attributes(cube_list)
 
month1_30year_file = cube_list.merge_cube()
month1_30year_collap_time = month1_30year_file.collapsed('time',iris.analysis.MEAN)
 
anomoly_month1_30year = month1_30year_file - month1_30year_collap_time
 
print(anomoly_month1_30year)

STD_NAMES['temp_anolmary'] = {'canonical_units': 'K'}

anomoly_month1_30year.standard_name = 'temp_anolmary'

iris.save(anomoly_month1_30year,'anomoly_30year.nc')

time_slice = anomoly_month1_30year.slices(['latitude', 'longitude'])

for_index_list = [list(time_slice),[x for x in range(30)]]
print(list(time_slice))

for i,j in zip(*for_index_list):
   plt.subplot(5,6,j+1)
   qplt.pcolormesh(i)
   plt.show()
 
equalise_attributes(cube_list)

month1_30year_file = cube_list.merge_cube()
month1_30year_collap_time = month1_30year_file.collapsed('time',iris.analysis.MEAN)

anomoly_month1_30year = month1_30year_file - month1_30year_collap_time
```
![image](https://user-images.githubusercontent.com/73323188/120260463-ea034100-c2d0-11eb-9ad4-9f5ebc433e18.png)

위 그림과 같이, 각 자료의 1월에서 총 30년동안의 1월의 평균값을 빼준 anomaly를 plot 하였다.

