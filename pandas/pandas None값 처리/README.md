## pandas None값 처리 

판다스는 다양한 형태와 형식으로 제공되기 때문에, 누락데이터를 처리함에 있어 유연성을 갖추는 것을 목표로한다.

pandas의 Nan값은 계산속도와 편의성을 이유로 기본 결측값 마커이지만, 부동소수점, 정수, bool값등 다양한 유형의 데이터와 함게 이 값을 쉽게 감지해야한다.

다음과 같은 DataFrame이 있을때,
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
notna를 통해 isna의 역의 결과를 얻을 수 있다.

```python
df.notna()
>>>
   name   job    age
0  True  True   True
1  True  True  False
2  True  True   True
3  True  True   True
4  True  True   True
5  True  True  False
```
이와 같이 data에 None값이 포함 된 경우, columns명으로 Seriese에 접근한뒤, fillna Method를 활용하여 None값을 지정 값으로 수정 할 수 있다.

## np.nan != None
np.nan != np.nan임에 주의하여 data를 처리해야한다.
```python
df['age'] == np.nan
>>>
0    False
1    False
2    False
3    False
4    False
5    False
Name: age, dtype: bool
```

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

## fillna의 인수
fillna에는 method라는 인수가 있다.

method를 활용하여, 인접해 있는 값으로 None 값을 처리 할 수 있다.

method인수 'ffill'는 forward fill을 의미하며, 앞의 값으로 None값을 채워준다.

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
    name    job age
0  Tomas   boss  30
1   Jane  woker  30
2   Mark   boss  33
3   Evan   boss  35
4   Lucy  woker  20
5   Jack  woker  20
```
첫번째, 두번째  None값이 앞의 값인 30과 20으로 각각 수정 되었다.

'bfill'은 backward fill을 의미하며, 뒤의 값으로 채워준다.
```python
df.fillna(method = 'bfill')
>>>
    name    job  age
0  Tomas   boss   30
1   Jane  woker   33
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker  NaN

```
df.fillna(method = 'bfill')의 결과와 같이, 앞이나 위의 값이 존재하지 않으면 None값은 그대로 남게 된다.

## limit 
limit 인수를 활용하여 바꾸고 싶은 None값의 개수를 설정 할 수 있다.

 다음과 같이 첫번째 None값만 바꿀수 있다.
```python
df.fillna('_',limit =1 )
>>>
    name    job  age
0  Tomas   boss   30
1   Jane  woker    _
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker  NaN
```
첫 번째 None값만 바뀐 것을 확인할 수 있다.

## __datetime NaT__

datetime값은 None값 처리 할 경우 결측값은 NaT로 처리된다.
```python
df = pd.Series([pd.Timestamp("20120101"),pd.Timestamp("20120101"),pd.Timestamp("20120101")],index=[0,2,4])
>>>
0   2012-01-01
2   2012-01-01
4   2012-01-01
dtype: datetime64[ns]
df.reindex([0,1,2,3,4])
>>>
0   2012-01-01
1          NaT
2   2012-01-01
3          NaT
4   2012-01-01
dtype: datetime64[ns]
```

## Nan값 산술계산
.sum()으로 데이터를 합칠 때, None값은 0으로 처리 되어 계산 된다.
```python
print(df)
>>>
      0     1     2
0     6  None    10
1     5     1     2
2     4     4  None
3     1     1     1
4  None    10     5

df[0].sum()
>>>
16

df[0].sum(skipna=0)
>>>
TypeError: unsupported operand type(s) for +: 'int' and 'NoneType'
```

None값이 계산에 포함되어, int와 NoneType은 계산될 수 없다는 메시지가 뜬다.
