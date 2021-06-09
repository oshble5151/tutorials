# bool data

pandas는 boolean data를 통해 indexing하는 것이 가능하다.

```python
s = pd.Series([1, 2, 3])
mask = pd.array([True, False, pd.NA], dtype="boolean")
s[mask]
>>>
0    1
dtype: int64
```

