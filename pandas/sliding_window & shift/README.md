# sliding window

sliding window는 두 포인터의 처음과 끝이 동일한 간격을 가지고 이동하는 것이다.

동일한 간격의 window가 slide 하며 배열의 일정 범위의 값을 비교할 때 유용한 알고리즘 이다.

시작점과 끝점의 두 포인터가 같은 간격으로 이동한다는 점에서, 두 포인터가 독립적으로 움직이는 two pointer 알고리즘과 차이가 있다.

# shift
pandas의 shift를 이용하면, sliiding window를 구현 할 수 있다.

shift를 사용하면 dataframe이 하나의 window가 되어 sliding 시킬 수 있다.

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
__1) period__ 

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
__2) fill_value__ 

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

__3) freq__ 

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
