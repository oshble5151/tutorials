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


# 로드 시 큐브에 메타데이터 추가 및 제거

## 메타데이터 로드 시 문제
## 메타데이터 양이 예상보다 많거나 적을 때 발생합니다.

# 1) 파일에 메타데이터가 충분하지 않을 때 
# 2) 파일의 메타데이터 중 일부가 파일 이름에 포함되어 있으나 실제 파일의 일부가 아님

# 3) Iris가 포맷을 제대로 처리하지 못하는 경우
