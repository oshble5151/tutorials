# iris & basemap를 활용한 전구 대기 특성값  plot

## python library를 활용한 대기property plot
1. 수치모델 연구 중, 북반구의 대기의 property 들이 북반구 해면 및 지면 온도에 미치는 영향 파악할 필요가 있었다.
2. 대기 property들의 예측값이 data로 들어있는 .nc 파일을 활용한다.
3. 총 30개년도의 모델 output(1980~2010) 자료를 평균낸다.
4. 평균된 자료에서 jja,djf 만을 뽑아 plot한다
5. 3~4 과정은 iris를 활용한다.



## 2m 대기온도
총 30개의 자료가 존재하며, 각 자료는 12개의 월별 값이 존재하는 month 자료이다.
자료는 time,latitude,longitude의 3차원 자료이다. 
```python
import iris
file = iris.load_cube('atmos_month_1981.nc')

file.shape
for i in f.coords():
    print(i.names[0])
>>> 
(12, 90, 144)
time
latitude
longitude
```
6월, 1월만 뽑아서 plot 해보기 위해서는 indexing이 필요하다.
간단하게 파이썬의 indexing을 사용하거나, iris의 extract를 활용 할 수 있다.
```python
iris.
```
전구 격자에 plot하기 위해서, 모든 월을 평균내어 2차원으로 만든 뒤 plot 해보았다.



