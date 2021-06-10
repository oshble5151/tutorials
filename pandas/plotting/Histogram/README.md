# Histogram
히스토그램은 도수분포표를 그림으로 나타낸 것으로, 가로축이 계급, 세로축에 도수가 들어간다. 

## 도수분포(Frequency table)
주어진 자료를 몇개의 계급으로 나누고, 각 계급의 도수를 조사하여 자료의 분포 상태를 나타낸 표

# Series hist plot
```python
df
>>>
           a         b         c
0    1.605596 -0.855900 -0.895566
1    0.817549  2.225235 -2.460565
2    2.364433  2.061507 -1.687245
3    1.540958  1.244500 -1.828496
4    0.181088  0.595832 -1.366294
..        ...       ...       ...
995  1.445188  1.059981 -0.461524
996  1.398968  0.046700 -0.320573
997  0.777838 -0.594835  0.158477
998  0.676614 -0.454325 -2.364796
999  2.241958 -0.457417  0.976776

print(df['a'].max(), df['a'].min())
>>>
4.21423983031402 -2.146363751253588
```
위의 dataframe에서 'a'column만을, 즉 Series객체를 hitogram으로 plot해보려 한다. 최대 최소값으로 계급구간의 범위를 확인하였다.
```python
df['a'].plot.hist()
![image](https://user-images.githubusercontent.com/73323188/121534421-2c005580-ca3c-11eb-92fb-dca71c8ced9f.png)
```

# Series hist plot
DataFrame을 hist로 plot하면, 모든 열의 histogram을 한 figure에 plot해준다.

```python
df.plot.hist()
```
![image](https://user-images.githubusercontent.com/73323188/121534631-5ce08a80-ca3c-11eb-8d7a-30a4a5359dad.png)
