## iris cube생성하기

시간,위도,경도 축을 가지는 3*5*5 size의 
기본적으로 다음과 같이 생성한다.
```
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
### 축 지정
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

## 축 data 확인 및 time축 units 지정 
축data는 다음과 같이 확인 할 수 있ㄷ.ㅏ
```python
48885,
