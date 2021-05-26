## anomaly

2m 온도 자료를 활용해서, 특정 값이 평균값과 얼마나 떨어져 있는지, 즉 anomaly를 보려고 한다.
자연과학에서 anomaly는 엘니뇨, 북방진동과 같은 현상에 있어 매우 중요한 요소이다.

다음 과정을 통해 anomaly를 구해보려고 한다.
1.  3차원의 자료에서 6,7,8 월의 자료만 추출한다. 
2.  6, 7, 8월의 자료를 time 축을 기준으로 평균내어 여름철을 대표하는 2차원의 jja 자료를 생성한다.
3.  6월, 7월, 8월에서 각각 jja를 뺀 결과, 즉 여름철 평균에 대한 anomlay를 확인하고 plot해본다.

iris가 numpy의 브로드 캐스팅을 따른다는 점을 활용하여, 3차원 자료에서 2차원 자료를 빼주어 간단하게 anomaly를 구할 수 있다.

다음과 같이 파일을 load한뒤 차원을 확인한다.
```python
import iris
file = iris.load_cube('atmos_month_1981.nc', tas)
print(file.coords())
print(file.shape)
>>>
DimCoord([1981-01-16 12:00:00, 1981-02-15 00:00:00, 1981-03-16 12:00:00,
       1981-04-16 00:00:00, 1981-05-16 12:00:00, 1981-06-16 00:00:00,
       1981-07-16 12:00:00, 1981-08-16 12:00:00, 1981-09-16 00:00:00,
       1981-10-16 12:00:00, 1981-11-16 00:00:00, 1981-12-16 12:00:00], ...
```
먼저 jja 파일을 만들기 위해, 파일을 load 함과 동시에 6,7,8월만을 추출해보려고 한다.
(12,)

time축이 12개인 자료임을 확인할 수 있다.

여름철 평균을 나타내는 자료를 만들기 위해, 다음과 같이 load와 동시에 6,7,8월을 추출할 수있다.
```python
jja_time = iris.Constraint(time = lambda cell: 6 <= cell.point.month <= 8)
file_month6_7_8 = iris.load_cube('atmos_month_1981.nc','tas'&jja_time)

print(file_month6_7_8.coord('time'))
print(file_month6_7_8.coord('time').shape)
>>>
DimCoord([1981-06-16 00:00:00, 1981-07-16 12:00:00, 1981-08-16 12:00:00], ...
(12,)
```
anomaly는 다음과 같이 구한다.
```python
jja_file =  file_month6_7_8.coolapsed('time')
print(jja_file.shape)
>>>
(90, 144)

anomaly = file_month6_7_8 - jja_file # 3차원에서 2차원 자료를 빼줌. broadcasting으로 인해 2차원 자료가 3차원 자료로 확장된 뒤 계산된다.
print(anomaly)
>>>
 <iris 'Cube' of unknown / (deg_k) (time: 3; latitude: 90; longitude: 144)>

```
## anomaly 시각화
```python
import matplotlib.pyplot as plt
from mpl_toolkits.basemap import Basemap

anomaly_6 = anomaly[0]
anomaly_7 = anomaly[1]
anomaly_8 = anomaly[2]

lon = anomaly.coord('longitude').points 
lat = anomaly.coord('latitude').points
x, y = m(*np.meshgrid(lon,lat))

m=Basemap(projection='mill',lat_ts=10,llcrnrlon=lon.min(), \
                 urcrnrlon=lon.max(),llcrnrlat=lat.min(),urcrnrlat=lat.max(), \
                 resolution='c')
                 
m.pcolormesh(x,y,anomaly[0],shading='flat',cmap=plt.cm.jet)
plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/119451200-f0913600-bd6f-11eb-8116-03fc39f1ac40.png)
6월의 anmaly가 plot 되었다. 마찬가지로 7,8월도 그려볼 수 있다.

![image](https://user-images.githubusercontent.com/73323188/119451351-1cacb700-bd70-11eb-9e48-80f4fb3f6cab.png)

![image](https://user-images.githubusercontent.com/73323188/119451564-5f6e8f00-bd70-11eb-9921-af51f5a68e2e.png)

