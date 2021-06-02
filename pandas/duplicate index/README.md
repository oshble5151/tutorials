# Duplicate index

__1) 중복 열 indexing__

Dataframe은 중복되는 열 또는 행을 가질 수 있다.

중복되는 행 혹은 열을 대상으로 indexing할 시, 차원이 감소하지 않는다.
```python
print(ds)
>>>
ds
a    0
b    1
b    2
dtype: int64

s1.loc['a']
>>>
0

s1.loc['b']
>>>
b    1
b    2
dtype: int64
```

__2) Duplicate index Detection __

index.is_unique : index혹은 columns에 
>>>python
s1
a    0
b    1
b    2

s1.index.is_unique

true










