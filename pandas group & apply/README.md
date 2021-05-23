## pandas apply 
다음과 같은 DataFrame이 있다.
```python
print(df)
>>>
    name    job  age
0  Tomas   boss   30
1   Jane  woker   22
2   Mark   boss   33
3   Evan   boss   35
4   Lucy  woker   20
5   Jack  woker   24
```
상사(boss)에게는 상사의 나이의 평균을, 근무자(woker)에게는 근무자 나이의 평균을 data에 추가하려고 한다.

```python
df['age_mean'] = df.groupby('job')['age'].transform('mean')
print(df)
>>> 
    name    job  age   age_mean
0  Tomas   boss   30  32.666667
1   Jane  woker   22  22.000000
2   Mark   boss   33  32.666667
3   Evan   boss   35  32.666667
4   Lucy  woker   20  22.000000
5   Jack  woker   24  22.000000
```
