# datetime_index, timezone 설정

pandas의 Datetimeindex는 timezone을 변경할 수 있다.


```python
print(datetime_index)
>>>  DatetimeIndex(['2021-01-31 00:00:00+00:00', '2021-02-28 00:00:00+00:00',
               '2021-03-31 00:00:00+00:00'],
              dtype='datetime64[ns, UTC]', freq='M')
              
datetime_index = datetime_index.tz_localize("UTC")

datetime_index.tz_convert("US/Pacific")
>>>
DatetimeIndex(['2021-01-30 16:00:00-08:00', '2021-02-27 16:00:00-08:00',
               '2021-03-30 17:00:00-07:00'],
              dtype='datetime64[ns, US/Pacific]', freq='M')
              
```
