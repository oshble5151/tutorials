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
file = file.collapsed('thickness', iris.analysis.SUM)
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

time 축을 기준으로 다시 축을 제거하면, 
```python
file=file.collapsed('time', iris.analysis.MEAN)
print(file)
>>>
ice concentration / (unknown)       (latitude: 200; longitude: 360)
     Dimension coordinates:
          latitude                           x               -
          longitude                          -               x
     Scalar coordinates:
          thickness: 0.55 meters, bound=(0.0, 1.1) meters
          time: 1981-07-02 12:00:00, bound=(1981-01-01 00:00:00, 1982-01-01 00:00:00)
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
          mean: time
```
2차원으로 축이 축소 되었으며, time축이 Scalar coordinates으로 변경되고 Cell methods mean을 사용했음을 확인 할 수 있다.

## 2)ferret을 활용한 격자 가중치를 이용한 평균값 확인 
먼저 다음과 같이 격자의 가중치를 고려했을 때의 올바른 해빙농도의 평균값을 ferret을 통해 확인해 보고자 한다

ferret은 @ave를 통해 평균을 계산해주는데, 기본적으로 격자 가중치를 고려하여 계산해준다.

ferret을 통해 자료의 CN(ice concentration)을 확인해보면, 

![image](https://user-images.githubusercontent.com/73323188/119293346-32957b80-bc8d-11eb-8740-44855a61d507.png)

위와 같이 x(longitude),y(latitude),k(thick),l(time) 축이 (360,200,5,12)인 자료임을 확인 할 수 있다.

![image](https://user-images.githubusercontent.com/73323188/119293392-4b9e2c80-bc8d-11eb-9ca0-bcd418136690.png)

위와 같이 k축은 합해주고, 나머지 축은 평균내준 결과, 해당 자료의 해빙농도는 0.04111로 계산 되었다.  

## 3) iris.analysis.cartography.area_weights를 활용한 평균값 계산
먼저 가중치를 주지 않고 iris에서 계산한 평균값을 보고자 한다.
```python
mean = file.collapsed(['latitude',longitude], iris.analysis.MEAN)
print(mean.data)
>>>
array(0.10828254)
```
ferret에서 계산한 값과 상당히 떨어진 값이 계산되었다.

이제 iris에서 격자 가중치를 주어 평균을 계산 해보고자 한다. 

먼저 cube의 축에 대해 다음과 같이 guess_bounds를 해주어야 한다.
```python
file('latitude').guess_bounds()
file('longitude').guess_bounds()
```
그렇지 않을 경우 다음과 같은 error가 발생한다.
```python
>>>
ValueError: Coordinates 'latitude' and 'longitude' must have bounds to determine the area weights.
```
guess_bounds를 해주고, 다음과 같이 격자 가중치를 고려한 평균을 계산할 수 있다.
```python
grid_areas = iris.analysis.cartography.area_weights(file)
grid_average_mean_cube = file.collapsed(['latitude','longitude'], iris.analysis.MEAN, weight=grid_areas)
print(grid_average_mean_cube.data)
>>>
array(0.04111394)
```
격자 가중치가 잘 반영되어, ferret의 값과 같은 평균값이 계산되었음을 확인할 수 있다.

참고로 ris.analysis.cartography.area_weights로 생성한 grid_areas를 확인 해보면, 자료와 같은 shape의 가중치 array를 확인할 수 있다.
```python
print(grid_areas)
print(grid_areas.shape)
>>>
array([[1.75042862e+09, 1.75044879e+09, 1.75050259e+09, ...,
        1.75050259e+09, 1.75044879e+09, 1.75042862e+09],
       [1.95457143e+09, 1.95459395e+09, 1.95465404e+09, ...,
        1.95465404e+09, 1.95459395e+09, 1.95457143e+09],
       [2.15811887e+09, 2.15814373e+09, 2.15821007e+09, ...,
        2.15821007e+09, 2.15814373e+09, 2.15811887e+09],
       ...,
       [7.37758637e+08, 7.37767138e+08, 7.37789817e+08, ...,
        7.37789817e+08, 7.37767138e+08, 7.37758637e+08],
       [5.03865603e+08, 5.03871409e+08, 5.03886898e+08, ...,
        5.03886898e+08, 5.03871409e+08, 5.03865603e+08],
       [3.71864479e+08, 3.71868764e+08, 3.71880195e+08, ...,
        3.71880195e+08, 3.71868764e+08, 3.71864479e+08]])
(200, 360)
```

    




 
