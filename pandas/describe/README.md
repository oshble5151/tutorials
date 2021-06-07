# pandas describe

describe method는 data의 분포 경향, 평균, 분산 등 다양한 통계량을 보여준다. (Nan값은 제외)

dtype에 따라 보여주는 통계량 목록이 다르다.

```python
ds = pd.Series([1,2,3,3,3,4,5,6,7])
>>>
0    1
1    2
2    3
3    3
4    3
5    4
6    5
7    6
8    7
dtype: int64

ds.describe() # dtype=int
>>>
count    9.000000
mean     3.777778
std      1.922094
min      1.000000
25%      3.000000
50%      3.000000
75%      5.000000
max      7.000000
dtype: float64

ds.astype(str).describe() # dtype=str
>>>
count     9
unique    7
top       3
freq      3
dtype: object
```
