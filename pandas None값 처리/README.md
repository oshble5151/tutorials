## pandas None값 처리 
다음과 같은 DataFrame이 있다.
```python
print(df)
>>>
    name    job   age
0  Tomas   boss    30
1   Jane  woker  None
2   Mark   boss    33
3   Evan   boss    35
4   Lucy  woker    20
5   Jack  woker  None
```
기본적으로 isna,isnull method를 통해 None값의 여부를 확인 할 수 있다.
```python
df.isna()
>>>
    name    job    age
0  False  False  False
1  False  False   True
2  False  False  False
3  False  False  False
4  False  False  False
5  False  False   True

df.isnull()
>>>
    name    job    age
0  False  False  False
1  False  False   True
2  False  False  False
3  False  False  False
4  False  False  False
5  False  False   True
```
이와 같이 data에 None값이 포함 된 경우, columns명으로 Seriese에 접근한뒤, fillna Method를 활용하여 None값을 지정 값으로 수정 할 수 있다.

```python
df['age'].fillna('-',inplace=bool(1))
print(df)
>>>
    name    job age
0  Tomas   boss  30
1   Jane  woker   -
2   Mark   boss  33
3   Evan   boss  35
4   Lucy  woker  20
5   Jack  woker   -
```
inplace인수를 활용하여 df에 바로 변경사항을 적용하였고 None값이 변경된 것을 확인 할수 있다.

일반적으로 df[df=='old'] = 'new' 처럼 numpy 스타일의 bool indexing을 통해 값을 변경할 수 있지만, None값은 이와 같은 방식으로 변경이 안 되기 때문에 fillna를 사용해주어야 한다. 
```python
df[df == 30] =35
print(df)
>>>
    name    job  age
0  Tomas   boss   35
1   Jane  woker  NaN
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker  NaN
```
age가 30인 값이 35로 바뀌었다. 동일한 방법으로 None값을 수정하면
```python
df[df==np.nan] ='_'
>>>
    name    job  age
0  Tomas   boss   35
1   Jane  woker  NaN
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker  NaN
```
위와 같이 numpy의 bool masking indexing 형식으로는 Nan값이 변하지 않다.

## fillna의 method 인수
fillna에는 method라는 인수가 있다.

method를 활용하여, 인접해 있는 값으로 None 값을 처리 할 수 있다.

method인수 'ffill'는 forward fill을 의미하며, 앞의 값으로 None값을 채워준다.

'bfill'은 backward fill을 의미하며, 뒤의 값으로 채워준다.
```python
print(df)
>>>
    name    job  age
0  Tomas   boss   30
1   Jane  woker  NaN
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker  NaN
df.fillna(method = 'ffill')
>>>
>>> df.fillna(method = 'ffill')
    name    job age
0  Tomas   boss  30
1   Jane  woker  30
2   Mark   boss  33
3   Evan   boss  35
4   Lucy  woker  20
5   Jack  woker  20
df.fillna(method = 'bfill')
    name    job  age
0  Tomas   boss   30
1   Jane  woker   33
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker  NaN

```
df.fillna(method = 'bfill')의 결과와 같이, 앞이나 위의 값이 존재하지 않으면 None값은 그대로 남게 된다.

