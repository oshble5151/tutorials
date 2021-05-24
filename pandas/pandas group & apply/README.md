## pandas group 
다음과 같은 DataFrame이 있다.
```python
print(df)
>>>
    name    job  age
0  Tomas   boss   30
1   Jane  woker   22
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker   24
```
상사(boss)에게는 상사의 나이의 평균을, 근무자(woker)에게는 근무자 나이의 평균을 data에 추가하려고 한다.
## transform method
transform method는 DataFrame(Series)의 method로서, Series나 DataFrame에 바로 사용할 수도 있고 groupby와 함께 사용 할수도 있다.

다음과 같이 lambda를 활용하여 값을 transform 해줄수 있다.

df['age']를 사용하면, 
```python
df['age'].transform(lambda x : x+1)
>>>
0    31
1    23
2    34
3    36
4    21
5    25
Name: age, dtype: int64
```
위와 같이 lamda가 적용되어 Series의 data값이 1씩 증가하였다.

groupby와 함께 사용하면, 다음과 같이 group별 평균값으로 값을 넣어줄 수 있다.

```python
df['age_mean'] = df.groupby('job')['age'].transform('mean')
print(df)
>>> 
    name    job  age   age_mean
0  Tomas   boss   30  32.666667
1   Jane  woker   22  22.000000
2   Mark   boss   33  32.666667
3   Evan   boss   35  32.666667
4   Lucy  woker   20  22.000000
5   Jack  woker   24  22.000000
```
각 그룹별의 평균값이 들어간 열이 추가되었음을 확인할 수 있다.

## apply
기본적으로 tarnsform과 같은 기능으로 쓸 수 있다.
```python
df['age_mean'].apply(lambda x : x+1)
>>>
0    31
1    23
2    34
3    36
4    21
5    25
Name: age, dtype: int64
```

apply를 사용하면 사용자 지정 함수로 Dataframe의 값을 평균낼 수 있다.
```python
print(df)
>>>
   a  b
0  1  4
1  2  5
2  3  6

def func(columns):
    x = columns[0]
    y = columns[1]
    z = columns[2]
    return (x+y+z) / df.shape[0]

df.apply(func)
>>>
a    2.0
b    5.0
dtype: float64
```

위와 같이, apply는 함수를 각 colums에 적용시켜 준다.

함수안에 print(columns) 추가해서 함수의 인자 columns를 확인 할 수 있다.
```python
def func(columns):
    print(columns)
df.apply(func)
>>>
0    1
1    2
2    3
Name: a, dtype: int64
0    4
1    5
2    6
Name: b, dtype: int64
a    None
b    None
dtype: object
```
이를 통해, 함수가 각 columns을 기준으로 적용되며, 모든 columns을 순환한다는 것을 알수 있다.

## apply 행기준 적용
axis 인자를 활용하면, 함수가 열을 순환하면서 적용되게 할 수 있고, 행을 순환하면서 적용되게 할 수도 있다.

```python
def func(columns):
    x = columns[0]
    y = columns[1]
    return (x+y) / df.shape[1]
df.apply(func,axis=1)
>>>
a    1
b    4
Name: 0, dtype: int64
a    2
b    5
Name: 1, dtype: int64
a    3
b    6
Name: 2, dtype: int64
0    2.5
1    3.5
2    4.5
dtype: float64
```
