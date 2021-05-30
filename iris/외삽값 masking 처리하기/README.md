# 외삽법, extrapolation
보외법 또는 외삽법(extrapolation)은 수학에서 원래의 관찰 범위를 넘어서는 변수의 값을 예측하는 방법이다. 

내삽법(interporation)은 관측되어 있는 두 x좌표 사이의 미지의 xi값에 대해서 f(xi)값을 예측한다는 점에서 외삽법과 차이가 있으며 

내삽법보다 더 큰 불확실성과 예측한 결과에 대한 신뢰성이 낮을 가능성이 있다.


# 작은 범위의 격자 자료 plot

iris cube의 regrid method는 일부 격자의 data를 전 지구 격자에 범위에 맞춰서 외삽해준다. 

이때 외삽되는 값으로는 None값이 들어가거나, 혹은 masking 처리 된다.

다음과 같이 전 위경도 범위의 자료와, 위도 -60 ~ 60, 동경 60 ~ 180, 서경 60 ~ 180 범위의 자료가 있다. 

```python
global_grid_data
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 90; longitude: 144)>

portion_grid_data
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 60; longitude: 95)>
```
portion_data를 plot해보면 다음과 같다. 
```python
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

x = portion_grid_data.coord('longitude').points
y = portion_grid_data.coord('latitude').points

m=Basemap(projection='mill',lat_ts=10,llcrnrlon=x.min(), \
          urcrnrlon=x.max(),llcrnrlat=y.min(),urcrnrlat=y.max(), \
                 resolution='c')

new_x, new_y = m(*np.meshgrid(x,y))
m.drawcoastlines()
m.pcolormesh(new_x, new_y,self.data,shading='flat',cmap=plt.cm.jet)
m.drawparallels(np.arange(-90., 120., 30.), labels=[1, 0, 0, 0])
m.drawmeridians(np.arange(-180., 180., 60.), labels=[0, 0, 0, 1])
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/120096021-25ccc800-c164-11eb-9d52-6cd6a31b17bf.png)

# None 값으로 외삽하여 전 격자에 plot 하기

regrid의 extrapolation_mode 인수를 사용하면, 일부격자의 data를 전 지구격자에 plot 할 수 있다.
```python
expolation = iris.analysis.Linear(extrapolation_mode='mask')

expolation_portion_data = portion_grid_data(global_grid_data,expolation)
```
expolation_portion_data를 plot 해보면 다음과 같이 외삽 범위가 전부 masking 처리 된것을 확인 할 수 있다.

![image](https://user-images.githubusercontent.com/73323188/120096163-d5099f00-c164-11eb-953e-67a36613883f.png)


