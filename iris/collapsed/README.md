# iris collapsed
collapsed는 축을 기준으로 계산하여 차원을 축소시킨 큐브를 반환해준다.

기준이 되는 축에 따라 반환값의 shape는 다르다.

다음과 같은 cube를 축에 따라 collapsed 할수 있다.

계산방법은 평균(MEAN)을 사용한다.
```python

print(file)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (time: 12; latitude: 90; longitude: 144)>
```
## __1) time축 collapsed__ 
```python
time_collapsed = file.collapsed('time',iris.analysis.MEAN)
print(time_collapsed)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (time: 12; longitude: 144)>
```
time 축을 중심으로 평균된 큐브가 반환 되었다.

이는 직관적으로, np.mean(file,axis=0)의 결과와 동일하다.


## __2) latitude축 collapsed__
```python
latitude_collapsed = file.collapsed('latitude',iris.analysis.MEAN)
print(latitude_collapsed)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (time: 12; longitude: 144)>
```
latitude축을 collapsed한 결과는 np.mean(file,axis=1)과 동일하다.

## __3) longitude축 collapsed__
```python
longitude_collapsed = file.collapsed('longitude',iris.analysis.MEAN)
print(longitude_collapsed)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (time: 12; latitude: 90)>
```
longitude축을 collapsed한 결과는 np.mean(file,axis=2)과 동일하다.

## __4) ['latitude','longitude'] 이중 축 collapsed__
```python
lat_lon_collapsed = file.collapsed('longitude',iris.analysis.MEAN)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (time: 12)>

lat_lon_collapsed.data == list(map(np.mean, file.data))
```
lat&lon 축으로 collapsed 한 결과는 map(np.mean,file.data)와 동일하다.

각 time 축에 대해 전 격자값을 평균낸 scalar값이 반환된다.

