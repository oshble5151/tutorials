# data값의 변경과 함께 단위 변경하기

iris를 활용하면 절대온도가 단위인 대기온도의 자료를 섭씨온도로 바꿀 수 있다.
```python
file = iris.load_cube('atmos_month_1981.nc','tas')
file.units
>>>
Unit('deg_k')
```
__1) unit attribute로 단위를 변환 __

속성에 다른 유닛값을 지정하는 방법이 있다. 이경우 데이터값은 변환되지 않는다.
```python
file.units = 'deg_c'

print(file.data)
print(file.units)
>>>
masked_array(
  data=[[[244.09712, 244.09712, 244.09712, ..., 244.09712, 244.09712,
          244.09712],
         [245.0632 , 245.0091 , 244.95386, ..., 245.21884, 245.16808,
          245.1162 ], ...
Unit('deg_c')
```
units은 'deg_c'로 바뀌었지만 데이터값은 그대로 Kelvin온도의 값이다.

__2) convert_units method로 단위를 변환 __

convert_units method를 사용해서 units을 바꾸면 데이터의 값도 자동으로 변환된다.

```python
file.convert_units('deg_c')
file.data
print(file.units)
>>>
masked_array(
  data=[[[-29.052877, -29.052877, -29.052877, ..., -29.052877,
          -29.052877, -29.052877],
         [-28.086798, -28.140905, -28.196142, ..., -27.931158,
          -27.981924, -28.033804], ...
deg_c
```


