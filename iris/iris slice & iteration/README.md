## cube iteration

iteration은 3차원 큐브 전체를 처리할 수 있는 유용한 방법이다.

3차원 큐브(z,y,x)를 처리하기 위해 3D 큐브를 구성하는 y와 x의 모든 2차원 슬라이스에 대해 반복할 수 있다.

iteration을 효율적으로 사용하기 위해, iris는 slice라는 기능을 제공한다.

시간, 위도, 경도 축이 12 by 90 by 144 size의 자료를 다음과 같이 slice 할 수 있다. 
```python
import iris
file = iris.load_cube('atmos_month_1981.nc')
print(file)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (time: 12; latitude: 90; longitude: 144)>

f_slice = f.slices(['latitude', 'longitude'])
print(list(f_slice))

print(len(f_slice))
>>>
[<iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 90; longitude: 144)>,
 <iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 90; longitude: 144)>,
                                    ...
 <iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 90; longitude: 144)>,
 <iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 90; longitude: 144)>]
 
 12
 ```
총 12개의 lon*lat 자료로 slice 된것을 확인 할 수 있다.

slice는 더 작은 차원의 개수로도 자를 수 있다.

위도축만 주어 slice 할경우는, 다음과 같다
```python
f_slice = f.slices(['latitude'])
slice_list = list(f_slice )
print(slice_list[0])
print(slice_list)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (latitude: 90)>
1728
```
위도축을 주어 slice 할 경우, 90개 지점의 위도자료가 하나의 1차원의 자료가 되어 경도의 개수 144개 만큼 slice 되는 것을 확인 할 수 있다.

time축이 총 12개 이므로, slice로 생성된 iterator에는 총 144 * 12(=1728)개의 자료가 담겨있는 것을 확인할 수 있다.

## 생성된 slice 자료 확인 및 plot
slice를 통해 생성된 자료는, slice시 기준으로 사용했던 축을 Dimension coordnation으로 가지고, 나머지 축은 scalarcoordination으로 가진다.

위도를 기준으로 slice한 파일의 축 정보를 확인해 보고자 한다.
```
slice_list[0]

print(slice_list)
>>>
temperature at 2 m / (deg_k)        (latitude: 90)
     Dimension coordinates:
          latitude                           x
     Scalar coordinates:
          longitude: 1.25 degrees_E, bound=(0.0, 2.5) degrees_E
          time: 1981-01-16 12:00:00, bound=(1981-01-01 00:00:00, 1981-02-01 00:00:00), ...
```
```python
import iris.plot as iplt
import iris.quickplot as qplt

lon_slice = slice_list[0:6]

for i in lon_slice:
    print(i.coord('longitude').points)
>>>
[1.25]
[3.75]
[6.25]
[8.75]
[11.25]
[13.75]

for_index_list = [lon_slice,[1,2,3,4,5,6],['1.25','3.75','6.25','8.75','11.25','13.25']]
for i,j,z in zip(*for_index_list): 
  plt.subplot(2,3,j)
  qplt.plot(i)
  iplt.citation('lat:'+z)
  plt.show()
```
![image](https://user-images.githubusercontent.com/73323188/119593900-c8f4a900-be15-11eb-830c-4580d5076317.png)