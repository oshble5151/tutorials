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
def lat_con(cell):
    ...:     
    ...:           return cell <= 20

con = iris.Constraint(latitude=lat_con)
con = iris.Constraint(latitude=lat_con , longitude = lon_con)

lat_con = lambda cell: cell <= 20 # lambda로 가능
```

# 속성도 제약 조건으로 사용가능

# 
