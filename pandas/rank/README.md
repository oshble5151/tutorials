# rank
rank method는 그룹에 대한 순위 평균이 할당된 데이터 순위를 생성한다.

다음과 같이 0~10까지의 random 배열의 숫자중에서 작은 수 부터 차례대로 순위를 매겨줄 수 있다.
```python
ds = pd.Series(np.random.choice(10,(10),0))
>>>
0    1
1    3
2    6
3    8
4    7
5    2
6    9
7    5
8    0
dtype: int32

ds.rank()
>>>
0     2.0
1     4.0
2     7.0
3     9.0
4     8.0
5     3.0
6    10.0
7     6.0
8     1.0
9     5.0
dtype: float64
```

DataFrame에도 사용할 수 있다. 이 경우 axis를 통해 열순위를 계산할지 행순위를 계산할지 지정할 수 있다.
