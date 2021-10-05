# 모든 큐브는  Cube.standard_name, Cube.long_name and Cube.units를 가진다.

# unit 변경법
```python
cube.convert_units('celsius') # 이 경우 값도 전환된다.
```
## 값은 바꾸고 싶지 않을 경우 cube.units을 직접 바꾸면 된다. 


# cube.cell_methods 
## 처리된 method는 f.cell_methods를 통해 확인 할 수 있다.
```python 
f.cell_methods
(CellMethod(method='mean', coord_names=('time',), intervals=(), comments=()),)
```


# cube coordinate name 보는법
```python
for i in f.coords():
  print( i.name())
>>>
'time'
'latitude'
'longitude'


coord_names = [x.name() for x in f.coords()]

>>> ['time', 'latitude', 'longitude']
```


# 축이 가지는 정보 
## 1) standard_name
## 2) long_name
## 3) units
## 4) points, bounds 를 가진다.
```python
t.points
>>> array([47848.5, 47849.5, 47850.5, ..., 52228.5, 52229.5, 52230.5])

t.bounds
>>> 
array([[47848., 47849.],
       [47849., 47850.],
       [47850., 47851.],
       ...,
       [52228., 52229.],
       [52229., 52230.],
       [52230., 52231.]])
```

