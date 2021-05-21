# 절기(JJA,DJF) 선택한뒤 file load
extract와 Constraint를 사용하면 자료의 필요한 월별에, 필요한 위경도만 선택하여 큐브를 생성할 수 있다.
## time 축 확인
```python 
import iris
file = iris.load_cube('atmos_month_1981.nc','tas')
file.coord('time').points 
print(file.coord('time'))
>>>
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
print(file.coord('time'))
>>>       
DimCoord([1981-06-16 00:00:00, 1981-07-16 12:00:00, 1981-08-16 12:00:00],...
```
jja(6,7,8) 만 추출되었다.

## load와 동시에 jja/djf 추출
