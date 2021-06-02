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

## 중복되는 index or columns 제거하기

__1) 단순히 제거하기__

boolean indexing을 이용해서 중복되는 행이나 열을 제거할 수 있다.
```python
print(df)
>>>
   A  B
a  1  4
b  2  5
b  3  6

df[~df.index.duplicated()]
>>>
   A  B
a  1  4
b  2  5
```
__2) groupby로 중복되는 index 산술 처리__

```python
print(df)
>>>
   A  B
a  1  4
b  2  5
b  3  6

df.groupby(level=0).mean()

>>>
     A    B
a  1.0  4.0
b  2.5  5.5
```
행을 기준으로 중복되는 lndex의 값들이 평균되었다.

열을 기준으로 중복되는 값을 탐지하고 처리하고 싶을 경우 axis 인수를 활용하면 된다.

```python
print(df)
>>>
   A  B   A   B
0  1  4  10  20
1  2  5  20  30
2  3  6  30  40

df.groupby(level=0, axis=1).mean()
>>>
      A     B
0   5.5  12.0
1  11.0  17.5
2  16.5  23.0
```
