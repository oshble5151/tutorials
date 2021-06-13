# 백분율 변화란
값의 변화를 원래의 값의 절대값으로 나눈 값에 100을 곱한것

![image](https://user-images.githubusercontent.com/73323188/121801646-4a9c6180-cc73-11eb-81b1-bc4ee1f4f4cb.png)


# pandas pct_change 

pct_change method를 통해, Series나 DataFrame의 백분율 변화값을 계산할 수 있다.

```python
ds = pd.Series([1,2,3,4,5])
ds.pct_change()
>>>
0         NaN
1    1.000000
2    0.500000
3    0.333333
4    0.250000
```
pct_change로 얻은 값에 100을 곱하면 백분율 변화값을 구할수 있다.

__period의 인수를 n값으로 줄때, 다음을 계산할 수 있다.__

![image](https://user-images.githubusercontent.com/73323188/121805517-8c82d300-cc86-11eb-9630-88b351aca319.png)

```python
ds.pct_change(2)
>>>
0         NaN
1         NaN
2    2.000000
3    1.000000
4    0.666667
dtype: float64
```
