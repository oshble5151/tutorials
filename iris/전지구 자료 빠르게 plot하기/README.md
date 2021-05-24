# iris & basemap를 활용한 전구 대기 특성값  plot

## python library를 활용한 대기property plot
1. 수치모델 연구 중, 북반구의 대기의 property 들이 북반구 해면 및 지면 온도에 미치는 영향 파악할 필요가 있었다.
2. 대기 property들의 예측값이 data로 들어있는 .nc 파일을 활용한다.
3. 평균된 자료에서 대기온도 변수를 추출하고 그 중에서 여름(jja)과 겨울(djf)을 대표하는 시간축 만을 뽑아 plot한다
4. 이 과정은 iris를 활용한다.



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
```
#python indexing
f[5] #6월 
f[0] #1월
```
```python
#iris.Constraint 와 extract 활용 
month_6 = iris.Constraint(time=lambda cell: cell.point.month ==6)
month_1 = iris.Constraint(time=lambda cell: cell.point.month ==1)

file_month6 = file.extract(month_6)
file_month1 = file.extract(month_1)

print(file_month6.coord('time'))
print(file_month1.coord('time'))
>>> DimCoord([1981-06-16 00:00:00] ... # 자료에서 6월만 추출됨
>>> DimCoord([1981-01-16 00:00:00] ... # 자료에서 1월만 추출됨
```
qplt를 활용하여 간단히 plot 할수 있다.

qplt는 cube를 인수로 넣어주면, 축 data를 자동으로 인식하여 title, color_bar와 함께 plot해준다.


```python
qplt.pcolormesh(file_month6)
plt.clf()
qplt.pcolormesh(file_month1)
```
# plot 결과
![5_21](https://user-images.githubusercontent.com/73323188/119101021-80bf3a80-ba53-11eb-8276-4b9017f6b345.png)

![5_21_djf](https://user-images.githubusercontent.com/73323188/119101389-e6132b80-ba53-11eb-8484-f266053a2f52.png)

## 시각화에 대한 최종 목표
생성된 그림은 qplt의 format을 따르기 때문에 다소 밋밋하다.

iris.cube.Cube 객체에 메써드 체인을 활용하여 basemap의 pcolormesh를 연결하고자 한다.

이를 통해 interactive형식으로 간단하게 시각화 하고자 한다.















