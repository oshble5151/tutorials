## julian -> gregorian
julian단위의 시간을 gregorian으로 보는 방법 2가지에 대해 작성해보고자 한다.

1) iris.coord('time')를 print 하는 방법
```python
f =iris.load_cube('atmos_month_1981.nc','tas')
f.coord('time')
>>>
DimCoord(array([47863.5]), bounds=array([[47848., 47879.]]), standard_name='time', units=Unit('days since 1850-01-01 00:00:00', calendar='julian')...
 
print(_)
>>>
DimCoord([1981-01-16 12:00:00], bounds=[[1981-01-01 00:00:00, 1981-02-01 00:00:00]],...
```
큐브를 생성할 때, print(사용자 생성큐브)로 time을 datetime 으로 보기 위해서는 cf_units을 사용하여 축 단위를 지정 해야한다. 
(-> [cube 생성](https://github.com/oshble5151/tutorials/tree/master/iris/cube%20%EC%83%9D%EC%84%B1))


2) datetime module을 사용하는 방법
```python
datetime.date(1850, 1, 1) + datetime.timedelta(days=47863.5)
>>>
datetime.date(1981, 1, 17)
```

