# Moving Mean - 이동평균
이동평균(롤링평균)은 전체 데이터 내의 여러 부분집합에 대한 평균을 만들어 데이터 요소를 분석하는 계산법이다.

예를 들어 다음과 같이 데이터가 있을때, 2개씩 이동평균한 결과는 다음과 같다.

![image](https://user-images.githubusercontent.com/73323188/120061026-226b0b00-c096-11eb-89d5-6a3557c84920.png)

이동평균은 산출할 데이터의 개수가 부족할 경우는 구할 수 없다.

3개씩 이동평균할 경우의 결과는 다음과 같다.

![image](https://user-images.githubusercontent.com/73323188/120061082-69f19700-c096-11eb-88c4-288c4b34bcde.png)

즉 순차적으로 이동해가며 datg를 더해주고, 부분집합의 수만큼 나누어 주는것이 이동평균의 개념이다.

## pandas rolling
이는 pandas의 rolling을 이용하여 간단하게 계산할 수 있다.

산출데이터의 개수가 3일 경우의 이동평균은 다음과 같이 구할 수 있다.
```python
ds = pd.Series([10,20,30,40,50])
ds.roling(window=3).mean()
>>>
0     NaN
1     NaN
2    20.0
3    30.0
4    40.0
dtype: float64
```

산출할 데이터의 개수보다 데이터의 개수가 작은 부분집합의 경우, Nan값이 지정된다.

min_periods 인수를 활용하면 산출할 데이터의 갯수를 부분집합내의 data 개수(Pn)에 맞춰주어 모든 부분집합에 대해 값을 계산할 수있다.

```python
test.rolling(window=3,min_periods=1 ).mean() # Pn이1개일 떄도 계산가능
>>> 
0    10.0
1    15.0
2    20.0
3    30.0
4    40.0
```
Pn이 1개 일때는 데이터를 1개, Pn이 2개일 때는 데이터를 2개 사용하여 이동평균이 계산되었다.

center을 사용하면, 결과를 window의 중간에 지정해준다.
```python
df = pd.Series(np.arange(10,130,10))
df.rolling(window=5).mean()
>>>
0       NaN
1       NaN
2       NaN
3       NaN
4      30.0
5      40.0
6      50.0
7      60.0
8      70.0
9      80.0
10     90.0
11    100.0
dtype: float64

df.rolling(window=5,center=True).mean()
0       NaN
1       NaN
2      30.0
3      40.0
4      50.0
5      60.0
6      70.0
7      80.0
8      90.0
9     100.0
10      NaN
11      NaN
dtype: float64
```
