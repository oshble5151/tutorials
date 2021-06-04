# pivot table
피벗 테이블(pivot table)은 데이터베이스, 스프레드시트, 비즈니스 인텔리전스 프로그램 등 다양한 데이터를 요약하는 통계표이다.

피벗 테이블은 데이터 처리의 한 기법이며, 유용한 정보에 집중할수 있도록 재정렬(pivot)하는 것을 의미한다.

# pd.pivot
다음과 같이 각 학생이 3일 동안 치른 시험 점수의 DataFrame이 있다.

## __1) pivot => values가 1개인 경우__ 
```python
print(df)
>>>
                  date  name  scores
0  2021-06-03 00:00:00   Tom      77
1  2021-06-04 00:00:00   Tom      34
2  2021-06-05 00:00:00   Tom      68
3  2021-06-03 00:00:00  Mary      15
4  2021-06-04 00:00:00  Mary      79
5  2021-06-05 00:00:00  Mary      38
6  2021-06-03 00:00:00   Ann      99
7  2021-06-04 00:00:00   Ann      99
8  2021-06-05 00:00:00   Ann      60
```
Tom의 성적만 보고 싶을 경우 다음과 같이 numpy style의 boolean indexing을 통해 볼 수 있다.
```python
df[df["name"] == "Tom"]
>>>
                  date name  scores
0  2021-06-03 00:00:00  Tom      77
1  2021-06-04 00:00:00  Tom      34
2  2021-06-05 00:00:00  Tom      68
```
pandas의 pivot을 사용하면 날짜에 따른 4학생의 점수를 다음과 같이 일목요연하게 확인 가능하다.
```python
df.pivot(index="date", columns="name",values="scores")
>>>
name        Ann  Mary  Tom
date                      
2021-06-03   99    15   77
2021-06-04   99    79   34
2021-06-05   60    38   68
```
## __2) pivot => values가 2개인 경우__ 
__2-1) value 열 추가__
먼저 각 날짜의 3명의 학생의 성적 평균과의 편차의 data가 담긴 열 'deviation'을 추가하려 한다.
```python

df.groupby('date').transform(np.mean) #각 날짜의 평균 data열 생성
print(df.groupby('date').transform(np.mean))
>>>
     scores 
0  63.666667
1  70.666667
2  55.333333
3  63.666667 
4  70.666667
5  55.333333
6  63.666667
7  70.666667
8  55.333333

df['deviation'] = df['scores'].values - df.groupby('date').transform(np.mean).iloc[:,0]
>>>
                  date  name  scores  deviation
0  2021-06-03 00:00:00   Tom      77  13.333333
1  2021-06-04 00:00:00   Tom      34 -36.666667
2  2021-06-05 00:00:00   Tom      68  12.666667
3  2021-06-03 00:00:00  Mary      15 -48.666667
4  2021-06-04 00:00:00  Mary      79   8.333333
5  2021-06-05 00:00:00  Mary      38 -17.333333
6  2021-06-03 00:00:00   Ann      99  35.333333
7  2021-06-04 00:00:00   Ann      99  28.333333
8  2021-06-05 00:00:00   Ann      60   4.666667
```
분산의 data가 담긴 열이 잘 추가 되었음을 확인 할 수 있다.

df.groupby('date').transform(sub_mean)은 DataFrame이므로, iloc를 사용해 Series로 변환시켜줘야 빼기 연산이 가능함에 유의 해야한다. 

__2-2) values가 2개인 pivot table 출력__

```python
df.pivot(index="date", columns="name")
>>>
              scores           deviation                      
name          Ann Mary Tom        Ann       Mary        Tom
date                                                       
2021-06-03     99   15  77  35.333333 -48.666667  13.333333
2021-06-04     99   79  34  28.333333   8.333333 -36.666667
2021-06-05     60   38  68   4.666667 -17.333333  12.666667
```
pivot 함수에서 index와 columns를 지정하고, values 인수가 누락될 경우, 모든 values가 pivot table에 나타난다.

이렇게 생성된 DataFrame에서 원하는 value만을 indexing해서 확인할 수 있다.
```python
two_value_pivot = df.pivot(index="date", columns="name")
two_value_pivot['deviation']
>>>
name              Ann       Mary        Tom
date                                       
2021-06-03  35.333333 -48.666667  13.333333
2021-06-04  28.333333   8.333333 -36.666667
2021-06-05   4.666667 -17.333333  12.666667
```
## __3) pivot table__ 

앞의 DataFrame은 6월3,4,5일에 각각 모든 학생이 한번씩 시험을 친 데이터가 들어있었다.

이번에는 조금 다르게, 3일에는 Tom만, 4일에는 Mary, 5일에는 Ann만 한명당 하루에 3번 시험을 본 데이터가 있다. 
```python
print(df)
>>>
                  date  name  scores  deviation
0  2021-06-03 00:00:00   Tom      77  13.333333
1  2021-06-04 00:00:00  Mary      34 -36.666667
2  2021-06-05 00:00:00   Ann      68  12.666667
3  2021-06-03 00:00:00   Tom      15 -48.666667
4  2021-06-04 00:00:00  Mary      79   8.333333
5  2021-06-05 00:00:00   Ann      38 -17.333333
6  2021-06-03 00:00:00   Tom      99  35.333333
7  2021-06-04 00:00:00  Mary      99  28.333333
8  2021-06-05 00:00:00   Ann      60   4.666667

df.pivot(index = 'date',columns='name')
>>>
    raise ValueError("Index contains duplicate entries, cannot reshape")
ValueError: Index contains duplicate entries, cannot reshape
```
이와 같은 경우 pivot 을 사용할 경우, date index, 즉 각 날짜에 시험을 친 사람이 같으므로 중복되어서 진행할 수 없다는 error가 발생한다.

