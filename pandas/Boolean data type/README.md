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

pd.NA값은 fillna(True)로 True값으로 변환할 수 있다. fillna로 False값은 변환 시킬 수 없다.

```python

s[mask.fillna(True)]
>>>
0    1
2    3
dtype: int64
```

# Kleene logical
![image](https://user-images.githubusercontent.com/73323188/121521914-8e068e00-ca2f-11eb-9265-60445e4f6833.png)

(출처:https://pandas.pydata.org/docs/user_guide/boolean.html#)
