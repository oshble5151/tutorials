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

## 생성 시 중복되는 label 허락 안하기 
set_flags를 활용하여 중복되는 label을 가질 경우 오류를 발생하게 할 수 있다.

```python

df = pd.DataFrame({"A": [0, 0, 2, 3]}, index=[0,0,1,2]).set_flags( allows_duplicate_labels=False)
>>>
Traceback (most recent call last):
  File "<pyshell#41>", line 1, in <module>
    df2 = pd.DataFrame({"A": [0, 1, 2, 3]}, index=[0,0,2,3]).set_flags( allows_duplicate_labels=False)
38\lib\site-packages\pandas\core\indexes\base.py", line 471, in _maybe_check_unique
                            ...
    raise DuplicateLabelError(msg)
pandas.errors.DuplicateLabelError: Index has duplicates.
      positions
label          
0        [0, 1]
```
속성에 bool값을 주어 중복값 허용여부를 바꿀 수도 있다.

insert를 활용해 중복값 허용 여부가 제대로 적용되는지 확인해볼 수 있다.
```python
print(df)
   A
0  0
1  1
2  2
3  3

df2.flags.allows_duplicate_labels = False
df2.flags.allows_duplicate_labels
>>>
False
```
df2.flags.allows_duplicate_labels = False를 통해 중복되는 label을 허용하지 않았다.

insert의 중복되는 name의 열의 추가를 허용해주는 allow_duplicates=True를 허용해서 열을 추가하려고 하면 다음과 같은 결과가 발생한다.
```python
df.insert(1,'A',[0,1,2,3],allow_duplicates=True)
>>>
Traceback (most recent call last):
  File "<pyshell#48>", line 1, in <module>
    df.insert(1,'A',[0,1,2,3],allow_duplicates=True)
  File "C:\Users\user\AppData\Local\Programs\Python\Python38\lib\site-packages\pandas\core\frame.py", line 3757, in insert
    raise ValueError(
ValueError: Cannot specify 'allow_duplicates=True' when 'self.flags.allows_duplicate_labels' is False.
```
allow_duplicates=True로 중복되는 열의 추가를 허용했음에도 불구하고, flags.allows_duplicate_labels가 False라서 수행할 수 없다는 오류를 볼 수 있다.

