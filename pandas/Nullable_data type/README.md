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
