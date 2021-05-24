## 데이터 수가 많을 경우의 apply적용

앞의 게시글에서 apply를 활용하여 DataFrame의 평균을 구했다.
기본적으로 열기준으로 평균을 구해주는 함수는 다음과 같다.
```python
def func(columns):
    x = columns[0]
    y = columns[1]
    z = columns[2]
    return (x+y+z) / df.shape[0]

# 데이터가 많아질 경우
def func(columns):
    print(columns)
    x = columns[0]
    y = columns[1]
    z = columns[2]  
         ...
    r = columns[99]
    return (x+y..+r) / df.shape[0]
```
가변인수를 활용하면, 다음과 같이 간단하게 작성 할 수 있다.
```python
print(df)
>>>
   a  b
0  1  4
1  2  5
2  3  6

def func(*columns):
  return sum(columns[0])/df.shape[0]

print(df.apply(func))
>>>
a    2.0
b    5.0
dtype: float64
```
*arg는 함수의 local 변수에 tuple로 저장되므로, return 에서 columns[0]으로 작성하여 tuple안의 값을 사용하게 해야함에 주의해야 한다.

마찬가지로 행기준의 평균도 구할 수 있다.
```python
def func(*columns):
  return sum(columns[0])/df.shape[1]

df.apply(func,1)
>>>
0    2.5
1    3.5
2    4.5
dtype: float64
```

## 90 by 144 자료에 적용

data의 개수가 많은 경우에 apply를 적용시키고자 한다.

data는 대기온도(2m)자료를 사용하였다.(위경도 90 by 144)

iris.collapse를 활용해서 간단하게 평균을 구할 수 있지만, DataFrame의 apply를 적용시켜 보기 위해 iris로 파일을 load한 뒤, pd.DataFrame으로 변환시켜보고자 한다. 

DataFrame 변환 작업은 iris.pandas.as_data_frame로 가능하다.

```python
file = iris.load_cube('atmos_month_1981.nc','tas')[0]
print(file.shape)
>>>
(90, 144)

df = iris.pandas.as_data_frame(file)

print(df)
>>>
                1.25        3.75        6.25        8.75    ...      351.25      353.75      356.25      358.75
-89.494382  244.097122  244.097122  244.097122  244.097122  ...  244.097122  244.097122  244.097122  244.097122
-87.977528  245.063202  245.009094  244.953857  244.897522  ...  245.268494  245.218842  245.168076  245.116196
-85.955056  246.768311  246.727295  246.685852  246.643967  ...  246.928101  246.888794  246.849075  246.808899
...                ...         ...         ...         ...  ...         ...         ...         ...         ...
 85.955056  242.115845  242.077927  242.039612  242.000900  ...  242.263550  242.227219  242.190491  242.153366
 87.977528  240.546295  240.496613  240.445923  240.394196  ...  240.734756  240.689163  240.642563  240.594940
 89.494382  239.659424  239.659424  239.659424  239.659424  ...  239.659424  239.659424  239.659424  239.659424
 ```
 apply를 적용시켜 열과 행에 대한 평균값을 각각 구해볼 수 있다.
```python
def func1(*columns):
    return sum(columns[0])/df.shape[0]
 
df.apply(func1) # 각 경도 지점에서의 전 위도범위의 평균값을 계산 
>>>
1.25      278.200718
3.75      278.102976
6.25      277.620331
8.75      277.261609
11.25     277.083877
             ...
348.75    279.122632
351.25    278.570816
353.75    278.263563
356.25    278.065438
358.75    278.131797
Length: 144, dtype: float64

def func2(*columns):
    return sum(columns[0])/df.shape[1]
 
df.apply(func2,1) # 각 위도 지점에서의 전 경도범위의 평균값을 계산 
>>>
-89.494382    246.423729
-87.977528    247.110905
-85.955056    249.975574
-83.932584    253.434462
-81.910112    255.403330
                 ...
 81.910112    241.347500
 83.932584    240.188036
 85.955056    238.977383
 87.977528    238.240834
 89.494382    238.053734
Length: 90, dtype: float64
```
위와 같이 전지구 자료에 apply를 적용시켜, 각 위도(경도)에 대한 전 경도(위도) 범위의 평균값을 계산 할 수 있다.

## apply로 인수가 여러개인 함수 사용

apply로 인수를 하나 더 추가해서 사용하는 방법도 간단하다.

분산을 구하는 함수를 만들어서 apply로 적용시키고자 한다.

```python
print(df)
>>>
   a  b
0  1  1
1  2  5
2  3  7
```
사실 numpy에서 분산을 구하는 함수가 존재하므로, 다음과 같이 분산을 간단하게 apply로 적용시킬 수 있다.
```python
df.apply(np.var)
>>>
a    0.666667
b    6.222222
dtype: float64
```
여기서는 apply가 적용되는 원리를 이해하기 위해 직접 분산을 구하는 함수를 작성해보자 한다.
```python

def var(*col,square):
	mean = sum(col[0])/df.shape[0]
	value = 0
	for i in col[0]:
		value += (i-mean)**square
	return value/df.shape[0]

df.apply(var,square=2)
>>>
a    0.666667
b    6.222222
dtype: float64
```
마찬가지로 행을 기준으로 적용시킬 수 도 있다.
```python
def var(*col,square):
	mean = sum(col[0])/df.shape[1]
	value = 0
	for i in col[0]:
		value += (i-mean)**square
	return value/df.shape[1]
df.apply(var,square=2, axis=1)
>>>
0    0.00
1    2.25
2    4.00
dtype: float64
```
