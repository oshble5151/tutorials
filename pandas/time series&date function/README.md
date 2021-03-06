# 
pandas는 모든 도메인에 대한 시계열 데이터를 처리하는 광범위한 기능을 제공한다.


__)resample__

index가 datetime일때 시간간격으로 추출할 수 있다.

```python
dt_index = pd.date_range("2018-01-01", periods=5, freq="H")

ds = pd.Series([0,1,2,3,4], index=dt_index)

ds.resample("2h").sum()
>>>
2018-01-01 00:00:00    1
2018-01-01 02:00:00    5
2018-01-01 04:00:00    4
Freq: 2H, dtype: int64
```
위와 같이 2시간 간격의 index간격으로 추출하여 합하거나, 평균내는 것이 가능하다.


__2) add day__

```python
dt = pd.Timestamp('2021-06-17 00:00:00') # Thurs day

dt.day_name()
>>> 'Thursday'
```

pd.offsets.BDay()를 사용하면, 주말을 제외하여 day를 더해줄 수 있다.
```python
dt_friday = pd.Timestamp('2021-06-18 00:00:00') # Fri day
dt_monday = dt_friday + pd.offsets.BDay()
dt_monday.day_name()
```

# pd.to_datetime

pd.to_datetime는 series 객체나 list객체를 받을 수 있다.

어떤 객체를 받는지에 따라 반환값의 type이 다르다.

```python
pd.to_datetime(pd.Series(["Jul 31, 2021", "2021-06-21", None]))
>>>
0   2021-07-31
1   2021-06-21
2          NaT
dtype: datetime64[ns]


pd.to_datetime(["2021/06/21", "2010.06.22"])
>>> DatetimeIndex(['2021-06-21', '2010-06-22'], dtype='datetime64[ns]', freq=None)

```

