# Duplicate index

## 중복 열 indexing

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

## Duplicate index Detection 

__1) index.is_unique : index혹은 columns에 중복값있는지 판별__
```python
s1
a    0
b    1
b    2

s1.index.is_unique
>>>
true
```

__2) index.duplicated() : index혹은 columns에 중복값있는지 판별__

index attribute에 duplicated()를 사용하면 중복되는 위치를 bool값으로 보여준다.

```python
s1.index.duplicated()
array([False, False,  True])
```








