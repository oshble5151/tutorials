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

```python
print(df)
>>>
    0   1   2   3   4   5   6   7   8   9
0  41  90  36  47   4   7  62   8  76  43
1  30  38  84  72  48  44  39  49  97  83
2   1  52  21  92   6   5  14  16   0  68
3  78  77   3  60  40  61  17  55  53  70
4  56  95  65  57  31  27  58  18  11  34
5  24  73  82  87  28  33  93  86  91  71
6  12  35  96  10  19  15  22  81   9  75
7  79  23  46  74  85  42  20  89   2  80
8  67  50  51  29  32  66  98  13  59  69
9  26  64  45  99  88  94  25  54  37  63

df.rank(axis=0)
>>>
      0     1     2     3     4     5     6     7     8     9
0   6.0   9.0   3.0   3.0   1.0   2.0   8.0   1.0   8.0   2.0
1   5.0   3.0   9.0   6.0   8.0   7.0   6.0   5.0  10.0  10.0
2   1.0   5.0   2.0   9.0   2.0   1.0   1.0   3.0   1.0   4.0
3   9.0   8.0   1.0   5.0   7.0   8.0   2.0   7.0   6.0   6.0
4   7.0  10.0   7.0   4.0   5.0   4.0   7.0   4.0   4.0   1.0
5   3.0   7.0   8.0   8.0   4.0   5.0   9.0   9.0   9.0   7.0
6   2.0   2.0  10.0   1.0   3.0   3.0   4.0   8.0   3.0   8.0
7  10.0   1.0   5.0   7.0   9.0   6.0   3.0  10.0   2.0   9.0
8   8.0   4.0   6.0   2.0   6.0   9.0  10.0   2.0   7.0   5.0
9   4.0   6.0   4.0  10.0  10.0  10.0   5.0   6.0   5.0   3.0

df.rank(axis=1)
>>>
      0     1     2     3    4    5     6     7     8    9
0   5.0  10.0   4.0   7.0  1.0  2.0   8.0   3.0   9.0  6.0
1   1.0   2.0   9.0   7.0  5.0  4.0   3.0   6.0  10.0  8.0
2   2.0   8.0   7.0  10.0  4.0  3.0   5.0   6.0   1.0  9.0
3  10.0   9.0   1.0   6.0  3.0  7.0   2.0   5.0   4.0  8.0
4   6.0  10.0   9.0   7.0  4.0  3.0   8.0   2.0   1.0  5.0
5   1.0   5.0   6.0   8.0  2.0  3.0  10.0   7.0   9.0  4.0
6   3.0   7.0  10.0   2.0  5.0  4.0   6.0   9.0   1.0  8.0
7   7.0   3.0   5.0   6.0  9.0  4.0   2.0  10.0   1.0  8.0
8   8.0   4.0   5.0   2.0  3.0  7.0  10.0   1.0   6.0  9.0
9   2.0   7.0   4.0  10.0  8.0  9.0   1.0   5.0   3.0  6.0
```

