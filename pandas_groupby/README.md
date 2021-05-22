## pandas groupby
pandas로 각 data를 같은 group으로 묶어줄 수 있다.

학생의 이름, 전공, 성별이 정보로 들어있는 DataFrame을 생성하였다.
```python
print(df)
>>>
      name        major  gender
0    jenny    Hydrology    male
1      Tom  Engineering  female
2   Nicole      Geology    male
3  Raechel    Hydrology  female
4  Simpson  Engineering    male
5     Yumi   Psychology  female
6     Adam    Hydrology    male
7   Vienna  Engineering  female
8    Simon   Psychology    male
9     Tina  Engineering  female
```
```python
group_majoor = df.groupby('gender')
print(group_majoor.groups)
>>>
{'Engineering': [1, 4, 7, 9], 'Geology': [2], 'Hydrology': [0, 3, 6], 'Psychology': [5, 8]}

print(group_majoor.size())
>>>
major
Engineering    4
Geology        1
Hydrology      3
Psychology     2
dtype: int64
```
group_majoor.groups, group_majoor.size()는 각각 dict와 pd.Series 형태로 group을 나타낸다.

pd.Series인 group_majoor.size()를 다음과 같이 'count'열을 추가한 DataFrame으로 만들 수 있다.
```python
df_major = pd.DataFrame({'count':group_major.size()})
print(df_major)
>>>
             count
major             
Engineering      4
Geology          1
Hydrology        3
Psychology       2
```
group_majoor.size()에 존재하던 major가 columns으로 인식되어 있지 않은채로 출력되었다.

이는 reset_index()로 깔끔하게 출력 할 수 있다.
```python
df = df_major.reset_index()
print(df)
>>>
         major  count
0  Engineering      4
1      Geology      1
2    Hydrology      3
3   Psychology      2
```



