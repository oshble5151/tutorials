## Datetime_index 생성하기
__1)date_range__

```python 
date_index = pd.date_range("20210101",periods=12,freq='M')
>>>
DatetimeIndex(['2021-01-31', '2021-02-28', '2021-03-31', '2021-04-30',
               '2021-05-31', '2021-06-30', '2021-07-31', '2021-08-31',
               '2021-09-30', '2021-10-31', '2021-11-30', '2021-12-31'],
              dtype='datetime64[ns]', freq='M')

df = pd.DataFrame(np.zeros((12,2)), index = date_index)
print(df)
>>>
              0    1
2021-01-31  0.0  0.0
2021-02-28  0.0  0.0
2021-03-31  0.0  0.0
2021-04-30  0.0  0.0
2021-05-31  0.0  0.0
2021-06-30  0.0  0.0
2021-07-31  0.0  0.0
2021-08-31  0.0  0.0
2021-09-30  0.0  0.0
2021-10-31  0.0  0.0
2021-11-30  0.0  0.0
2021-12-31  0.0  0.0
```
 
__2)to_datetime__

```python
dti = pd.to_datetime(["31/1/2021", np.datetime64("2021-02-28"), datetime.datetime(2021, 3, 31)])
```
pandas는 dateitme_index를 만들때 문자열, np.datetime64, datetime 객체등을 받아들일 수 있다.


