## pandas group
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

pd.Series인 group_majoor.size()를 'count'열을 추가한 DataFrame으로 만들 수 있다.
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
