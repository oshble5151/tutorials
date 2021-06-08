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

__1)percentiles__

percentiles 인수를 활용하여 분율의 범위를 정해줄수 있다. default값은 [.25, .5, .75]이다.
```python
ds.describe(percentiles = [.3,.6,.9])
>>>
count    9.000000
mean     3.777778
std      1.922094
min      1.000000
30%      3.000000
50%      3.000000
60%      3.800000
90%      6.200000
max      7.000000
dtype: float64
```
__2)datetime_is_numericd__

datetime_is_numericd는 datatime type을 숫자형 data로 간주할 지 문자형으로 간주할지 결정하는 인수이다.
```python
ds_date = pd.Series([
       np.datetime64("2019-06-07"),
       np.datetime64("2020-06-07"),
    np.datetime64("2021-06-07")])
>>>
print(ds_date)
0   2019-06-07
1   2020-06-07
2   2021-06-07
dtype: datetime64[ns]

s.describe() 
>>>
count                       3
unique                      3
top       2021-06-07 00:00:00
freq                        1
first     2019-06-07 00:00:00
last      2021-06-07 00:00:00
dtype: object
```
datetime 형식의 data를 문자열로 간주하고 decribe가 실행되었다.

```python
s.describe(datetime_is_numeric=True)
>>>
count                      3
mean     2020-06-06 16:00:00
min      2019-06-07 00:00:00
25%      2019-12-07 00:00:00
50%      2020-06-07 00:00:00
75%      2020-12-06 12:00:00
max      2021-06-07 00:00:00
dtype: object
```

## DataFrame 일때

dataframe일때 describe는 다음과 같이 출력된다.
```python
df = pd.DataFrame({'blood_type':'A B O AB O B'.split(' '),'weight':[66,75,53,72,55,68]},index = 'Tom Matthew Ann Jack chris Michael'.split(' '))
print(df)
>>>
        blood_type  weight
Tom              A      66
Matthew          B      75
Ann              O      53
Jack            AB      72
chris            O      55
Michael          B      68

print(df.describe())
>>>
          weight
count   6.000000
mean   64.833333
std     8.975894
min    53.000000
25%    57.750000
50%    67.000000
75%    71.000000
max    75.000000
```
dataframe에 describe를 사용할 경우 기본적으로 numeric, 즉 숫자형 데이터로 구성된 열에 대해서만 통계량을 보여준다.

문자열 data로 구성된 열의 요약을 보고 싶을때는, 다음과 같이 include 변수를 활용할 수 있다.
```python
print(df.describe(include='all'))
>>>

       blood_type     weight
count           6   6.000000
unique          4        NaN
top             O        NaN
freq            2        NaN
mean          NaN  64.833333
std           NaN   8.975894
min           NaN  53.000000
25%           NaN  57.750000
50%           NaN  67.000000
75%           NaN  71.000000
max           NaN  75.000000

df.describe(include='object') # print only string columns
df.describe(include=np.number) # print only numeric columns

```

describe를 통해 category형 자료의 요약만 볼 수 있다.
```python
df.describe(include='category')
df['weight'] = df['weight'].astype('category')

df.describe(include='category')
>>>
        weight  
count        6
unique       6
top         53
freq         1
```
