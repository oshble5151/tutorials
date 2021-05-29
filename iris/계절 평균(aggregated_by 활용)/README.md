## 계절별(JJA,DJF) 자료
data의 자료를 볼때, 계절별로 나누어서 확인해야 할때가 있다.

다음과 같이 대기온도(2m) 자료를 load하고, time 축과 shape를 확인한다.
```python
file = iris.load_cube('atmos_month_2001.nc')
print(file.coord('time'))
print(file.shape)
>>>
DimCoord([2001-01-16 12:00:00, 2001-02-15 00:00:00, 2001-03-16 12:00:00,
       2001-04-16 00:00:00, 2001-05-16 12:00:00, 2001-06-16 00:00:00,
       2001-07-16 12:00:00, 2001-08-16 12:00:00, 2001-09-16 00:00:00,
       2001-10-16 12:00:00, 2001-11-16 00:00:00, 2001-12-16 12:00:00], ...
(12,90,144)
```
(iris에서는 time 축을 print하면 datetime형식으로 변환하여 출력해준다. [Julian -> gregorian으로 변경하기](https://github.com/oshble5151/tutorials/tree/master/Julian%20-%3E%20gregorian%EC%9C%BC%EB%A1%9C%20%EB%B3%80%EA%B2%BD%ED%95%98%EA%B8%B0)
)


12달의 위경도 90 by 144의 자료가 들어있음을 확인할 수 있다.


## 계절 추출 및 ~
온도나 단파복사량과 같은 대기 변수는 가장 뚜렷할 때인 여름철과 겨울철을 확인해 볼 필요가 있다.

1.계절을 대표하기 위해, 12달에서 필요한 달의 자료를 추출한다.(여름:6,7,8월,겨울:12,1,2월)

2.추출된 파일을 time축으로 평균낸다. (여름: 6,7,8월 평균 => jja, 겨울: 12,1,2 평균 => DJF)

위 과정은 다음과 같이 코드를 작성하여 진행 할 수 있다.
```python
import iris.coord_categorisation
iris.coord_categorisation.add_season(file,'time',name = 'clim_season') # file에 clim_season 축을 추가
print(file)
>>>
temperature at 2 m / (deg_k)        (time: 12; latitude: 90; longitude: 144)
     Dimension coordinates:
          time                           x             -              -
          latitude                       -             x              -
          longitude                      -             -              x
     Auxiliary coordinates:
          clim_season                    x             -              -
     Attributes: ...

print(file.coord('clim_season'))
>>>
AuxCoord(array(['djf', 'djf', 'mam', 'mam', 'mam', 'jja', 'jja', 'jja', 'son',
       'son', 'son', 'djf'], dtype='<U64'), standard_name=None, units=Unit('no_unit'), long_name='clim_season', attributes={'calendar_type': 'JULIAN', 'cartesian_axis': 'T'})
```
time축에 대한 보조축인 clim_season이 추가된 것을 확인할 수 있다.

clim_season 축을 기준으로 평균을 내고자 하는 경우 aggregated_by를 활용하여 가능하다.
```python
seasonal_mean = f.aggregated_by('clim_seasons',iris.analysis.MEAN) 
print(seasonal_mean)
>>>
<iris 'Cube' of temperature at 2 m / (deg_k) (-- : 4; latitude: 90; longitude: 144)>
```
위와 같이 각 계절별 평균 cube 4개가 생성된 것을 확인할 수 있다.
