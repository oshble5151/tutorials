# median
median은 중앙값을 의미한다.

어떤 주어진 값들을 크기의 순서대로 정렬했을 때 가장 중앙에 위치하는 값을 의미한다. 

pandas를 활용해 중앙값을 구할 수 있다.

```python
import pandas as pd 

ds = pd.Series([42,40,38,37,43,39,78,38,45,44,40,38,41,62,61,44,50])
ds.median()
>>> 42
```
