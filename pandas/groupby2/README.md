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




