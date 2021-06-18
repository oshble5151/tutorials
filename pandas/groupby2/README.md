# 중복된 index에 대한 group화 

판다스는 중복된 index에 대한 group화가 가능하다.

```python
index = [0,1,2] *2
ds = pd.Series([1,2,3,10,20,30,100,200,300], index)

grouped = ds.groupby(level=0)

grouped.first()
>>>
1    1
2    2
3    3
dtype: int64

grouped.last()
>>>
1    100
2    200
3    300
dtype: int64

다음과 같이 group에 대한 평균이 가능하다.
```

```python
grouped.mean()

1     37
2     74
3    111
```

동일한 index 번호끼리 평균되었다.

groupby를 사용하면 다음과 같이 지정한 열에서 특정 행의 값을 뽑아 낼 수 있다.

다음과 같이 남자와 여자의 키가 들어간 data frame이 있을때, 남자의 키만 보려면 다음과 같이 할 수 있다. 
```python
df= pd.DataFrame({"gender": ["man", "woman", "woman", "man"], "tall": [177, 165, 155, 180]})

df.groupby(['gender']).get_group('man')
>>>
  gender  tall
0    man   177
3    man   180
```

# groupby dropna

다음과 같이 남성과 여성의 키와 몸무게가 들어있는 dataframe이 있을때, 키를 그룹화 할 수 있다.
```python
df
>>>
  gender   tall  weight
0    man  177.0      75
1  woman    NaN      55
2  woman  155.0      40
3    man  180.0      90

       weight
tall         
155.0      40
177.0      75
180.0      90

```
위와 같이 어떤 특성을 기준으로 그룹화할때, 기본적으로 None값의 행을 제외하고 결과를 보여준다.

None값도 보고 싶으면 다음과 같이 dropna=False로 주면 된다.

```python
df.groupby('tall',dropna=False).sum()
       weight
tall         
155.0      40
177.0      75
180.0      90
NaN        55
```

# groupby attribute
```python
df
>>>
  gender   tall  weight
0    man  177.0      75
1  woman    NaN      55
2  woman  155.0      40
3    man  180.0      90

df.groupby('gender').groups
>>>
{'man': [0, 3], 'woman': [1, 2]}
```
위와 같이 group과 index가 들어간 딕셔너리가 반환됨을 알 수 있다.
