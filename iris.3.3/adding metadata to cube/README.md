# 큐브에 메타데이터 추가하기

## 1) Cube.add_dim_coord
## 2) Cube.add_aux_coord
## 3) Cube.remove_coord

# 스칼라 좌표로 만드는 법

```python
new_coord = iris.coords.AuxCoord(1, long_name='my_custom_coordinate', units='no_unit')
>>>
Scalar coordinates:
        forecast_period             0.0 hours
        forecast_reference_time     2006-06-15 00:00:00
        my_custom_coordinate        1
        time                        2006-06-15 00:00:00
```
