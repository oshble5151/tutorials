# loading multiple files
```python
filenames = [iris.sample_data_path('uk_hires.pp'),
             iris.sample_data_path('air_temp.pp')]
cubes = iris.load(filenames)
```

# Constrained Loading

## NameConstraint

## 로드시 좌표값을 제한할 수 있다.

```python
filename = iris.sample_data_path('uk_hires.pp')
level_10_or_16_fp_6 = iris.Constraint(model_level_number=[10, 16], forecast_period=6)
cubes = iris.load(filename, level_10_or_16_fp_6)

```
```python
def lat_con(cell):
    ...:     
    ...:           return cell <= 20

con = iris.Constraint(latitude=lat_con)
con = iris.Constraint(latitude=lat_con , longitude = lon_con)

lat_con = lambda cell: cell <= 20 # lambda로 가능
```

# 속성도 제약 조건으로 사용가능

# Constraining on Time
## 월 추출 하기

```python
hour_11 = iris.Constraint(time=lambda cell: cell.point.hour == 11)

cube= cube.extract(hour_11)
```


## 시간 범위로 extract하기

```python

pdt1 = PartialDateTime(year=2004, month=1)
pdt2 = PartialDateTime(year=2004, month=7)

con = iris.Constraint(
    time=lambda cell: pdt1 <= cell.point < pdt2)
f.extract(con)
```
