## pandas로 중복데이터 삭제하기
다음과 같이 0번과 10번 index값이 중복되는 DataFrame이 있다.
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
10   jenny    Hydrology    male
```
duplicated method를 통해, 중복여부를 확인 할 수 있다.
```python
df.duplicated()
>>>
0     False
1     False
2     False
3     False
4     False
5     False
6     False
7     False
8     False
9     False
10     True
dtype: bool
```
drop_duplicates method를 사용하여 모든 columns의 값이 완전히 일치하는 값을 제거 할 수 있다.
```python
df.drop_duplicates()
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
inplace 인수를 사용하면 DataFrame에 바로 적용 가능하다.
```python
df.drop_duplicates(inplace=True)
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
duplicated는 default의 경우 모든 열의 값이 일치하는 경우만 중복으로 인식한다. 

옵션을 통해, 특정 열의 값만 중복되도 중복으로 인식하게 할 수 있다.

다음과 같이 major만 같은 경우를 중복으로 인식하게 할 수 있다.
```python
df.duplicated(['major'])
>>>
0    False
1    False
2    False
3     True
4     True
5    False
6     True
7     True
8     True
9     True
dtype: bool
```
마찬가지로 drop_duplicates를 활용하여, major만 같은 경우에도 중복값을 제거시켜 줄 수 있다.
```python
df.drop_duplicates(['major'])
>>>
     name        major  gender
0   jenny    Hydrology    male
1     Tom  Engineering  female
2  Nicole      Geology    male
5    Yumi   Psychology  female
```
이 경우 중복 된 것 중 가장 처음 것만 남고 삭제 된것을 볼 수 있다.

keep 인수를 활용하면, 중복되는 것 중 나중의 것을 남길 수 도 있다.
```python
df.drop_duplicates(['major'], keep = 'last')
>>>
     name        major  gender
2  Nicole      Geology    male
6    Adam    Hydrology    male
8   Simon   Psychology    male
9    Tina  Engineering  female
```
