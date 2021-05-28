## grouby 
(* .tsv 자료는 부경대학교 지오데이터 분석 수업의 자료를 활용하였다.)

grouby는 그룹을 결정하는데 사용되며 다음 3가지 프로세스를 실행가능하다.

**1. Splitting : 데이터를 몇가지 기준으로 나눔**

**2. Applying : 각 그룹에 대한 독립적인 함수 적용**

**3. Combining : 결과를 데이터 구조로 변환함**

## Splitting
Splitting 과정을 통해, 데이터를 간단하게 분할 할 수 있다.



## Applying
Applying단계에서는, 다음을 수행 가능하다.
**1. Transformation : 그룹별로 계산을 수행해준다.
**2. Filtration : 

```python
print(df)

groupy는 열에만 적용되지만, index가 multi_index인 경우 행에도 지원된다.

```python
import pandas as pd
df = pd.read_csv('gapminder.tsv',sep='\t')
print(df)
>>>
          country continent  year  lifeExp       pop   gdpPercap          new
0     Afghanistan      Asia  1952   28.801   8425333  779.445314  5195.484004
1     Afghanistan      Asia  1957   30.332   9240934  820.853030  5787.732940
2     Afghanistan      Asia  1962   31.997  10267083  853.100710  5729.369625
3     Afghanistan      Asia  1967   34.020  11537966  836.197138  5971.173374
4     Afghanistan      Asia  1972   36.088  13079460  739.981106  8187.468699
...           ...       ...   ...      ...       ...         ...          ...
1699     Zimbabwe    Africa  1987   62.351   9216418  706.157306  2282.668991
1700     Zimbabwe    Africa  1992   60.377  10704340  693.420786  2281.810333
1701     Zimbabwe    Africa  1997   46.809  11404948  792.449960  2378.759555
1702     Zimbabwe    Africa  2002   39.989  11926563  672.038623  2599.385159
1703     Zimbabwe    Africa  2007   43.487  12311143  469.709298  3089.032605

[1704 rows x 7 columns]
```
## groupby.get_group
get_group을 통해 보고 싶은 group만 볼 수 있다.
```python
df.groupby('continent').get_group('Asia')
>>>
          country continent  year  lifeExp       pop    gdpPercap           new
0     Afghanistan      Asia  1952   28.801   8425333   779.445314   5195.484004
1     Afghanistan      Asia  1957   30.332   9240934   820.853030   5787.732940

...           ...       ...   ...      ...       ...          ...           ...
1678  Yemen, Rep.      Asia  2002   60.308  18701257  2234.820827  10174.090397
1679  Yemen, Rep.      Asia  2007   62.698  22211743  2280.769906  12473.026870
[396 rows x 7 columns]
```
대륙이 Asia 인 자료만 추출 되었음을 확인할 수 있다.

Asia 중에서도 1952년의 gdp만 보고 싶을경우 

이 경우 grouping을 2개 주면 가능하다. 
```python
df.groupby(['continent','year']).get_group(('Asia',1952))
>>>
                country continent  year   ...        pop      gdpPercap          new
0            Afghanistan      Asia  1952  ...    8425333     779.445314  5195.484004
84               Bahrain      Asia  1952  ...     120447    9867.084765  5195.484004
                                          ...   
1656  West Bank and Gaza      Asia  1952  ...    1030585    1515.592329  5195.484004
1668         Yemen, Rep.      Asia  1952  ...    4963829     781.717576  5195.484004
[33 rows x 7 columns]
```
grouping이 2개 일때는 tuple로 값을 넣어줘야 함에 유의해야한다.

## grouping한 자료에서 특정 열만 보고 싶을 경우
```python
df.groupby(['continent','year']).get_group(('Asia',1952))['gdpPercap']
>>>
0          779.445314
84        9867.084765
         ...
1656      1515.592329
1668       781.717576
Name: gdpPercap, dtype: float64
```
## filter

gdp의 평균을 다음과 같이 구할 수 있다.
```python 
df['gdpPercap'].mean()
>>>
7215.327081212149
```

자료 전체 gdp값의 평균을 확인하였다. 이 중 gdp의 평균이 7000 이상인 곳만 보고 싶을 경우 filter를 사용하여 다음과 같이 확인할 수 있다.
```python
df.groupby('continent').filter(lambda x : x['gdpPercap'].mean() > 7000)




