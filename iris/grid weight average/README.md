## 격자 가중치 평균 (grid weight average)
전지구 격자에서, 격자 별로 부여된 가중치는 모두 다르다.

이 가중치를 고려하지 않고 iris.analysis.MEAN을 사용하여 평균을 낼 경우 정확하지 않은 값을 얻을 수 있다.

200by360 사이즈의 해빙농도 자료를 사용하여, 격자 가중치를 고려한 경우와 그렇지 않은 경우를 비교해 보려한다

## 1) 축 제거(collapsed)
먼저 file을 load한 후 파일의 shape와 축을 확인한다.
```python
file = iris.load_cube('ice_month_1981.nc')
print(file.shape)
print(file)
>>>
(12, 5, 200, 360)
ice concentration / (unknown)       (time: 12; thickness: 5; latitude: 200; longitude: 360)
     Dimension coordinates:
          time                           x              -            -               -
          thickness                      -              x            -               -
          latitude                       -              -            x               -
          longitude                      -              -            -               x
     Attributes:
          filename: ice_month.nc
          grid_tile: N/A
          grid_type: regular
          invalid_units: 0-1
          time_avg_info: average_T1,average_T2,average_DT
          title: KIOST_ESM_PI-Control-CMIP6
     Cell methods:
          mean: time

```
Dimension coordinates에 time, thickness, latitude, longitude 총 4개의 축이 존재하는 것을 확인할 수 있다.

자료 data의 평균값을 구하기 위해 축을 줄여 주어야 한다.

해당 파일의 자료는 thickness축이 존재하므로, 해빙의 농도의 평균을 구하기 위해서 우선 thickness축을 중심으로 합해주어야 한다.

다음과 같이 collapsed method를 활용하여 합해줄수 있다.
```python
file.collapsed('thickness', iris.analysis.SUM)
print(file)
>>>
ice concentration / (unknown)       (time: 12; latitude: 200; longitude: 360)
     Dimension coordinates:
          time                           x             -               -
          latitude                       -             x               -
          longitude                      -             -               x
     Scalar coordinates:
          thickness: 0.55 meters, bound=(0.0, 1.1) meters
     Attributes:
          filename: ice_month.nc
          grid_tile: N/A
          grid_type: regular
          invalid_units: 0-1
          time_avg_info: average_T1,average_T2,average_DT
          title: KIOST_ESM_PI-Control-CMIP6
     Cell methods:
          mean: time
          sum: thickness
```

iris.analysis.SUM을 사용하여 차원을 줄여주었다.

thickness 축은 Dimension coordinates에서 Scalar coordinates 축으로 변환 되었고, Cell methods의 SUM을 통해 축을 줄이는 과정에서 data를 모두 합해주었음을 확인할 수 있다.

위 과정을 통해 얻은 3차원에서 다음과 같이 하나의 평균값을 얻을 수 있다.
```python




 
