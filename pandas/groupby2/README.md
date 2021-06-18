# 중복된 index에 대한 group화 

판다스는 중복된 index에 대한 group화가 가능하다.

```python
index = [0,1,2] *2
ds = pd.Series([1,2,3,10,20,30,100,200,300], index)

grouped = ds.groupby(level=0)

grouped.first()
>>>
1    1
2    2
3    3
dtype: int64

grouped.last()
>>>
1    100
2    200
3    300
dtype: int64

다음과 같이 group에 대한 평균이 가능하다.
```

```python
grouped.mean()

1     37
2     74
3    111
```

동일한 index 번호끼리 평균되었다.

groupby를 사용하면 다음과 같이 지정한 열에서 특정 행의 값을 뽑아 낼 수 있다.

다음과 같이 남자와 여자의 키가 들어간 data frame이 있을때, 남자의 키만 보려면 다음과 같이 할 수 있다. 
```python
df= pd.DataFrame({"gender": ["man", "woman", "woman", "man"], "tall": [177, 165, 155, 180]})

df.groupby(['gender']).get_group('man')
>>>
  gender  tall
0    man   177
3    man   180
```

# groupby dropna

다음과 같이 남성과 여성의 키와 몸무게가 들어있는 dataframe이 있을때, 키를 그룹화 할 수 있다.
```python
df
>>>
  gender   tall  weight
0    man  177.0      75
1  woman    NaN      55
2  woman  155.0      40
3    man  180.0      90

       weight
tall         
155.0      40
177.0      75
180.0      90

```
위와 같이 어떤 특성을 기준으로 그룹화할때, 기본적으로 None값의 행을 제외하고 결과를 보여준다.

None값도 보고 싶으면 다음과 같이 dropna=False로 주면 된다.

```python
df.groupby('tall',dropna=False).sum()
       weight
tall         
155.0      40
177.0      75
180.0      90
NaN        55
```

# groupby attribute
```python
df
>>>
  gender   tall  weight
0    man  177.0      75
1  woman    NaN      55
2  woman  155.0      40
3    man  180.0      90

df.groupby('gender').groups
>>>
{'man': [0, 3], 'woman': [1, 2]}
```
위와 같이 group과 index가 들어간 딕셔너리가 반환됨을 알 수 있다.

# grouby

__1) 그룹을 1개 줄 경우__

```python
df
>>>
     A      B         C         D
0  foo    one -1.287808 -0.354624
1  bar    one -0.696100 -0.499489
2  foo    two -0.143256 -0.609751
3  bar  three -0.663622 -1.653208
4  foo    two -0.280383 -1.806659
5  bar    two  0.120506 -2.009116
6  foo    one -0.073835 -0.159918
7  foo  three -0.587425  0.376111

grouped = df.groupy("A")
>>>

            C         D
A                      
bar -1.239216 -4.161813
foo -2.372706 -2.554841
```

__2) 그룹을 2개 줄 경우__

```python
grouped = df.groupy(["A","B"])
>>>
                  C         D
A   B                        
bar one   -0.696100 -0.499489
    three -0.663622 -1.653208
    two    0.120506 -2.009116
foo one   -1.361643 -0.514542
    three -0.587425  0.376111
    two   -0.423639 -2.416410
```
2개의 열로 groupby할 경우, Mltiindexing된 dataFrame이 반환된다.

다음과 같이 Multi_index dataframe이 있을때, __level__을 통해 group화 할 수 있다.

```python
df
                  C         D
A   B                        
foo one   -1.287808 -0.354624
bar one   -0.696100 -0.499489
foo two   -0.143256 -0.609751
bar three -0.663622 -1.653208
foo two   -0.280383 -1.806659
bar two    0.120506 -2.009116
foo one   -0.073835 -0.159918
    three -0.587425  0.376111

df.groupby(level ="A").sum()
>>>
            C         D
A                      
bar -1.239216 -4.161813
foo -2.372706 -2.554841

df
>>>
     A      B         C         D
0  foo    one -1.287808 -0.354624
1  bar    one -0.696100 -0.499489
2  foo    two -0.143256 -0.609751
3  bar  three -0.663622 -1.653208
4  foo    two -0.280383 -1.806659
5  bar    two  0.120506 -2.009116
6  foo    one -0.073835 -0.159918
7  foo  three -0.587425  0.376111

df2
>>>
                  C         D
A   B                        
foo one   -1.287808 -0.354624
bar one   -0.696100 -0.499489
foo two   -0.143256 -0.609751
bar three -0.663622 -1.653208
foo two   -0.280383 -1.806659
bar two    0.120506 -2.009116
foo one   -0.073835 -0.159918
    three -0.587425  0.376111

df.groupby("A").sum()
>>>
            C         D
A                      
bar -1.239216 -4.161813
foo -2.372706 -2.554841

df2.groupby(level ="A").sum()
>>>
            C         D
A                      
bar -1.239216 -4.161813
foo -2.372706 -2.554841
```
위와 같이 df.groupby("A").sum()와 df2.groupby(level ="A").sum()(multi_indexing)의 결과는 같음을 알 수 있다.


