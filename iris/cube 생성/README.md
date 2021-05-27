## iris cube생성하기

시간,위도,경도 축을 가지는 3*5*5 size의 해수면 온도를 가지는 자료를 생성해보고자 한다.
기본적으로 다음과 같이 생성한다.
```python
import iris
import numpy as np
array = np.random.choice(75,(3,5,5),0)
file = iris.cube.Cube(array)
>>>
<iris 'Cube' of unknown / (unknown) (-- : 3; -- : 5; -- : 5)>
```
data attribute를 활용하여, data 값을 확인 할 수 있다.
```python
file.data
>>>
array([[[31,  8, 47, 66, 29],
        [ 2, 11,  9, 15, 52],
        [56,  1, 36, 55, 72],
        [64, 20, 25, 10, 48],
        [ 6,  0, 22, 13, 18]],

       [[60, 58, 12,  3, 67],
        [34, 38, 71, 73, 21],
        [42, 28, 23, 70, 53],
        [ 7, 46, 45, 49, 35],
        [68, 40, 16, 27, 33]],

       [[54, 32, 17, 50, 69],
        [37, 63, 57, 65, 44],
        [19, 51, 62, 74, 61],
        [30, 39,  4, 24, 59],
        [43, 26, 14, 41,  5]]])
```
## 축 지정 및 metadata 확인
현재 생성된 큐브는 축에 대한 metadata가 들어있지 않아 Unkown으로 표시되고 있다.

축은 iris.coord를 사용하여 다음과 같이 지정해 줄 수 있다.
```python
time = iris.coords.DimCoord(['48885','48886','48887'])
lat = iris.coords.DimCoord(np.linspace(82.5,90.5,5))
lon = iris.coords.DimCoord(np.linspace(160.5,180.5,5))

file.add_dim_coord(time,0)
file.add_dim_coord(lat,1)
file.add_dim_coord(lon,2)
print(file)
>>>
<iris 'Cube' of unknown / (unknown) (time: 3; latitude: 5; longitude: 5)>
```
축이 잘 지정된 것을 확인 할 수 있다.
 
축에 대한 meta data들은 다음과 같이 확인 할 수 있다. 
```python
file.coord('time')
file.coord('time').points
file.coord('time').units
>>>
DimCoord(array([48885, 48886, 48887]), standard_name='time', units=Unit('1'))
array([48885, 48886, 48887])
Unit('1')
```

## time축 units 지정 
축을 생성할때 unit을 정해주지 않으면 기본적으로 1이 들어간다. 이 경우 print 사용 시 다음과 같이 처음 입력했던 Julian 단위의 시간을 변환 없이 보여준다.
```python
print(file.coord('time'))
>>>
DimCoord(array([48885, 48886, 48887]), standard_name='time', units=Unit('1'))
```
cf_units을 사용하여 다음과 같이 축지정을 해줄 수 있다.
```python
time_coord_unit = cf_units.Unit('days since 1850-01-01 00:00:00', calendar='julian')
file.coord('time').units = time_coord_unit
print(file.coord('time'))
>>>
DimCoord([1983-11-04 00:00:00, 1983-11-05 00:00:00, 1983-11-06 00:00:00], standard_name='time', calendar='julian')
```
위와 같이 축을 바꾸어서, 우리에게 익숙한 date-time 형식으로 시간축의 값을 확인해 볼수 있다. 

## standard name 지정

위에서 standard name이 Unkown인 것을 확인 하였다.

standard name은 merge 할때 지정되어있어야 하거나, qplt로 plot할때 자동으로 title로 사용되기 때문에, 지정해주는 것이 유용하다.

축의 name은 iris의 std_names 모듈에 지정되어 있는 문자열 객체로 사용해야 한다.

이는 다음과 같이 확인 가능하다.
```python
import iris.std_names as std 
std.STD_NAMES.keys()
>>>
dict_keys(['acoustic_signal_roundtrip_travel_time_in_sea_water', 
           'aerodynamic_particle_diameter', 'aerodynamic_resistance',
           'aerosol_angstrom_exponent', 'age_of_sea_ice' ...
```
대기 온도에 대한 큐브로 만들기 위해, air_temperature를 standard name으로 주고, 섭씨(celsius)를 units으로 주려고 한다.
```python
file.standard_name = 'sea_surface_temperature'
file.units='celsius'
print(file)
>>>
<iris 'Cube' of air_temperature / (celsius) (time: 3; latitude: 5; longitude: 5)>
```

마지막으로, 실제 해수온도와 유사한 데이터 값으로 주기 위해, 15~18도의 범위로 데이터를 바꾸려고 한다.
dube의 데이터는 masked array형태로 제공되며, 다음과 같이 간단하게 값을 바꾸어 줄 수 있다.

```python

sea_temp = np.random.choice(np.arange(16,18,0.25),(3,5,5),1)

file.data = sea_temp 
print(file.data)
>>>
array([[[15.  , 16.75, 16.75, 16.25, 15.75],
        [17.5 , 17.  , 16.75, 17.  , 17.25],
        [15.  , 17.25, 17.  , 16.5 , 15.25],
        [15.75, 16.5 , 15.75, 17.5 , 16.75],
        [17.5 , 17.75, 17.25, 17.75, 17.5 ]],

       [[16.5 , 17.25, 17.5 , 16.5 , 17.25],
        [16.75, 15.25, 15.  , 16.75, 17.75],
        [17.  , 15.25, 15.5 , 17.25, 16.  ],
        [16.5 , 17.75, 15.75, 15.75, 15.75],
        [16.  , 16.  , 16.5 , 17.25, 15.25]],

       [[15.5 , 15.5 , 16.25, 15.75, 16.75],
        [16.75, 17.5 , 16.25, 15.  , 17.75],
        [15.75, 15.75, 15.25, 16.25, 15.25],
        [15.75, 15.  , 17.  , 15.  , 15.  ],
        [15.25, 17.  , 15.75, 16.75, 16.75]]])
 ```

