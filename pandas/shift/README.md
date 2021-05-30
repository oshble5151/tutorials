# pandas shift

shift를 이용하면, 열을 아래 방향으로 이동시킬 수 있다.

이때 빈 data 위치는 Nan값으로 채워진다.
```python
df
>>>
     0    1    2
0  1.0  2.0  3.0
1  4.0  5.0  6.0
2  7.0  8.0  9.0
3  NaN  NaN  NaN
4  NaN  NaN  NaN
5  NaN  NaN  NaN

df.shift(1)
>>>
     0    1    2
0  NaN  NaN  NaN
1  1.0  2.0  3.0
2  4.0  5.0  6.0
3  7.0  8.0  9.0
4  NaN  NaN  NaN
5  NaN  NaN  NaN
```
__1) period

period로 이동시킬 간격을 지정 가능 하다.
```python
df.shift(2)
>>>
     0    1    2
0  NaN  NaN  NaN
1  NaN  NaN  NaN
2  1.0  2.0  3.0
3  4.0  5.0  6.0
4  7.0  8.0  9.0
5  NaN  NaN  NaN
```
__2) fill_value

fill_value를 지정하여 Nan값 대신 다른 값으로 빈 행을 채워줄 수 있다.
```python
df.shift(2,fill_value=0)
>>>
     0    1    2
0  0.0  0.0  0.0
1  0.0  0.0  0.0
2  1.0  2.0  3.0
4  4.0  5.0  6.0
5  7.0  8.0  9.0
3  NaN  NaN  NaN
```

__2) freq 

freq는 index가 datetime_index이고 index만 shift 시키고 싶을 때 사용한다.

```python
df
>>>
                       0    1    2
2021-01-01 00:00:00  1.0  2.0  3.0
2021-01-01 01:00:00  4.0  5.0  6.0
2021-01-01 02:00:00  7.0  8.0  9.0
2021-01-01 03:00:00  NaN  NaN  NaN
2021-01-01 04:00:00  NaN  NaN  NaN
2021-01-01 05:00:00  NaN  NaN  NaN

df.shift(freq='2h')
>>>
                       0    1    2
2021-01-01 02:00:00  1.0  2.0  3.0
2021-01-01 03:00:00  4.0  5.0  6.0
2021-01-01 04:00:00  7.0  8.0  9.0
2021-01-01 05:00:00  NaN  NaN  NaN
2021-01-01 06:00:00  NaN  NaN  NaN
2021-01-01 07:00:00  NaN  NaN  NaN
```
index만 shift되었다.

shift는 axis인수를 활용하여 index도 shift 시킬수 있다.
