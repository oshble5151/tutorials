# 중복된 index에 대한 group화 

판다스는 중복된 index에 대한 group화가 가능하다.

```python
index = [0,1,2] *2
ds = pd.Series([1,2,3,10,20,30], index)

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

