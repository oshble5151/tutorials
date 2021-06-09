#

판다스에서 NaN은 float type이므로, 결측값이 있는 정수 배열은 type이 강제적으로 float type이 된다.
```python
print(pd.Series([1,2,3]))
>>>
0    1
1    2
2    3
dtype: int64

print(pd.Series([1,2,3,None]))
>>>
0    1.0
1    2.0
2    3.0
3    NaN
dtype: float64
```
# pd.Int64Dtype

이 경우 dtype 인수를 pd.Int64Dtype()를 지정하여 정수형으로 표현가능하다.

(__* pd.Int64Dtype()의 alias로 "Int64"도 가능하다.__)

```python
pd.Series([1, 2, np.nan], dtype="Int64")
0       1
1       2
2    <NA>
dtype: Int64
```
# pd.array

pd.array를 기본적으로 결측값이 있는 정수데이터를 int type 으로 그대로 표현할 수 있다.
```python
pd.array([1,2,None])
>>>
<IntegerArray>
[1, 2, <NA>]
Length: 3, dtype: Int64

pd.Series(pd.array([1,2,None]))
0    1.0
1    2.0
2    NaN
dtype: float64
```

