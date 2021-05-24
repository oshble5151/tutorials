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

data는 위경도 90 by 144의 자료를 사용하였다.

iris.collapse를 활용해서 간단하게 평균을 구할 수 있지만, DataFrame의 apply를 적용시켜 보기 위해 

iris로 파일을 load한 뒤 pd.DataFrame으로 변환시켜보고자 한다. 

DataFrame 변환 작업은 iris.pandas.as_data_frame로 가능하다.

```python
file = iris.load_cube('atmos_month_1981.nc','tas')[0]
print(file.shape)
>>>
(90, 144)
