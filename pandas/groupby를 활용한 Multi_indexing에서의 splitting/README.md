# Multi_indexing splitting

pandas의 groupby를 통해, data를 group으로 구분하는 spliting을 할 수 있다.

본 게시글에서는 Multi_indexing을 가진 data를 splitting하는 방법을 알아보고자 한다.

다음과 같이 한국, 미국, 일본 3나라 학생들의 익명의 시험테스트 결과가 data로 들어있는 DataFrame이 있다.

```python
print(df)
>>>
  gender  country  Math  English
0    man    Korea    90       35
1  women    Korea    45       40
2    man  America    15       70
3  women    Japan    25       35
4    man  America    10       90
5  women  America    70       25
6    man    Korea    75       55
7    man    Japan     5       50

```

set_index를 통해 성별과 나라의 정보가 담긴 Muti_indexing을 생성할 수 있다.
```python
df = df.set_index(["gender", "country"])
print(df)
>>>
                Math  English
gender country
man    Korea      90       35
women  Korea      45       40
man    America    15       70
women  Japan      25       35
man    America    10       90
women  America    70       25
man    Korea      75       55
       Japan       5       50
```

성별에 관계없이 국가별로 구분지어 학생들의 점수의 평균을 보고 싶은 경우, 다음과 같이 지정된 index를 제외한 index를 기준으로 그룹화할 수 있다.
```python
grouped = df2.groupby(level=df2.index.names.difference(["gender"]))
grouped.mean()
>>>
              Math    English
country
America  31.666667  61.666667
Japan    15.000000  42.500000
Korea    70.000000  43.333333
```
위와 같이 국가별로 그룹화하여 평균점수가 계산되었다.

위의 코드는 다음과 같이 포함하고 싶은 열을 넣어주면 더 간단하게 작성가능하다.
```python
grouped = df2.groupby('country')
grouped
>>>
              Math    English
country
America  31.666667  61.666667
Japan    15.000000  42.500000
Korea    70.000000  43.333333
```
