# 절기(JJA,DJF) 선택한뒤 file load
extract와 Constraint를 사용하면 자료의 필요한 월별에, 필요한 위경도만 선택하여 큐브를 생성할 수 있다.
## time 축 확인
```python 
import iris
file = iris.load_cube('atmos_month_1981.nc','tas')
print(file)

file.coord('time').points 
print(file.coord('time'))
>>>
temperature at 2 m / (deg_k)        (time: 12; latitude: 90; longitude: 144)
array([47863.5, 47893. , 47922.5, 47953. , 47983.5, 48014. , 48044.5,
       48075.5, 48106. , 48136.5, 48167. , 48197.5])
       
DimCoord([1981-01-16 12:00:00, 1981-02-15 00:00:00, 1981-03-16 12:00:00,
       1981-04-16 00:00:00, 1981-05-16 12:00:00, 1981-06-16 00:00:00,
       1981-07-16 12:00:00, 1981-08-16 12:00:00, 1981-09-16 00:00:00,
       1981-10-16 12:00:00, 1981-11-16 00:00:00, 1981-12-16 12:00:00],...
```
1. 자료의 file.coord('time')을 print하면, datetime형식으로 출력됨.

2. 12개의 월별 자료가 들어있다.

## jja/djf 추출 - 
```python 
jja = iris.Constraint(time = lambda cell: 6 <= cell.point <= 8)
file_jja =  file.extract(jja)
file_djf =  file.extract(djf)
print(file.coord('time'))
>>>       
DimCoord([1981-06-16 00:00:00, 1981-07-16 12:00:00, 1981-08-16 12:00:00],...
```
jja(6,7,8) 만 추출되었다.

## load와 동시에 jja/djf 추출
```python 
file = iris.load_cube('atmos_month_1981.nc','tas'&jja)
file = iris.load_cube('atmos_month_1981.nc','tas'&djf)
```
결과는 마찬가지로 jja,djf(12,1,2)만 load와 동시에 추출된다.

## + 위경도 동시 추출

위도와 경도도 Constraint를 사용하면 load와 동시에 추출 가능하다.

현재 진행중인 연구는 북반구 대륙에서의 온도변화를 중심으로 진행되기 때문에,

북위 30~90의 범위만 추출하고자 한다.
```python 
lat = iris.Constraint(latitude=lambda cell: 30 <= cell <= 90) 
file = iris.load_cube('atmos_month_1981.nc','tas'&jja&lat)
print(file)
>>>
temperature at 2 m / (deg_k)        (time: 3; latitude: 31; longitude: 144) ...
```
6,7,8월의 자료를 평균 내어 2차원 자료로 만든 뒤, plot 해볼수 있다.
```python
new_file = file.collapsed('time',iris.analysis.MEAN)
qplt.pcolormesh(new_file)
```

