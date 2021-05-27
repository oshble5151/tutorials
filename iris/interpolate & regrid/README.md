# iris - interpolate 
내삽법을 통해 관측된 좌표의 값을 추측하여 관측되지 않은 좌표의 값을 추측할 수 있다.

iris의 interpolate는 scipy의 scheme을 기반으로 한다.

본 게시글에서는 선형보간법(iris.analysis.Linear)을 다룬다.

interpolation을 하기 위해서는 다음 2가지 인수가 필요하다.

1. sample point
2. scheme

# sample point 가 위도 경도 모두 포함할때
다음과 같은 위경도 90*144의 2차원 큐브가 있을때,
```python
import iris
file = iris.load('atmos_month_1981.nc','tas')
print(f.coord('latitude').points[70:72])
>>>
array([51.57303371, 53.59550562])
```
자료의 위도의 일부를 볼때 위와 같은 간격으로 격자가 존재함을 확인하였다.

sample point를 위도와 경도차원 모두 주어, 존재하지 않는 격자지점인 **(위도:52.25, 경도:0)** 포인트에서의 값을 interpolate 할 수있다.

이처럼 한 격자의 값을 내삽법으로 추측하고 싶을때 다음과 같이 interpolate 할 수 있다.

sample point를 위도와 경도에 모두 부여할 필요는 없다. 

```python
sample_points = [('latitude', 52.25), ('longitude', 0)]
file.interpolate(sample_points, iris.analysis.Linear()).data
>>>
array(277.53668, dtype=float32)
```
위와 같이 존재하지 않는 한 격자에서의 값이 내삽되었음을 확인할 수 있다.

# sample point 가 하나만 주어질때
예를 들어 sample point를 위도 축에만 주면, 아래의 2차원 격자그림과 같이 한 위도 지점에서의 전 경도 범위의 값을 내삽 할수 있다.

![image](https://user-images.githubusercontent.com/73323188/119830375-2b919600-bf37-11eb-995e-7e0a9f435325.png)
```python
sample_points = [('latitude', 52.25)]
f.interpolate(sample_points, iris.analysis.Linear()).data
f.interpolate(sample_points, iris.analysis.Linear()).data.shape
>>>
masked_array(data=[277.7911071777344, 277.8486633300781,
                   276.8140563964844, 275.1882629394531, ... ]
(144,)
```
존재하지 않았던 위도 52.25지점에서, 경도축의 개수 144개 만큼의 값이 내삽되었다.

# sample point의 value가 array로 주어질때
내삽 되길원하는 위 경도의 범위를 배열로 줄수 있다.

다음과 같이 대기온도에 대한 90 * 144 size의 예측값이 있고, 241 * 480 size의 관측값이 있다.

관측값과 예측값의 차이를 보고 싶은데, iris cube는 size가 같은 경우만 연산이 가능하다.

이 경우 내삽을 통해서 90 * 144 자료를 241 * 480 size로 확장 시켜줄 필요가 있다.

```python
observe_data = iris.load_cube('era_1981.nc','t2m') #240*480 size
predict_data = iris.load_cube('atmos_month_1981.nc','tas') #90*144 size

sample_points = [('latitude', observe_data.coord('latitude').points),('longitude',observe_data.coord('longitude').points)]

new_predict = predict_data.interpolate(sample_points, iris.analysis.Linear())
print(new_predict.size)
>>>
(240,480)
```
![image](https://user-images.githubusercontent.com/73323188/119834710-29c9d180-bf3b-11eb-84c3-68275166d907.png)
![image](https://user-images.githubusercontent.com/73323188/119834794-3ea66500-bf3b-11eb-918d-c69e852aaa77.png)

