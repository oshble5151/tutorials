# 데이터 열 추가하기

## location(loc)
loc indexting을 활용하여 간단하게 값을 지정 할 수 있다.
```python
print(df)
>>>
df
   col1
0     4
1     8
2     1

df.loc[:,'new_col'] = [0,0,0]
>>>
   col1  new_col
0     4        0
1     8        0
2     1        0
```
loc를 열을 추가 할때 다음과 같이 간단하게 기존에 존재하던 열의 제곱값을 가진 열을 새로 추가할 수 있다.
```python
df.loc[:,'pow_col'] = df['col1']**2
>>>
   col1  pow_col
0     4       16
1     8       64
2     1        1
```
## 2. df.insert 
insert를 활용하면 열의 순서를 지정하여 추가해줄 수 있다.
```python
print(df)
>>>
   col1  col2  col2
0   0.0   0.0   0.0
1   0.0   0.0   0.0
2   0.0   0.0   0.0
```

```python
df.insert(0,'new_col',[0]*3)
>>>
   new_col  col1  col2  col2
0        0   0.0   0.0   0.0
1        0   0.0   0.0   0.0
2        0   0.0   0.0   0.0
```
같은 열을 추가해줄 경우, 이미 존재한다는 오류가 발생한다.

이 경우 allow_duplicates를 사용해서 이미 존재하는 열을 추가 해줄수 있다.
```python
df.insert(0,'new_col',[0]*3,allow_duplicates=True)
>>>
   new_col  new_col  col1  col2  col2
0        0        0   0.0   0.0   0.0
1        0        0   0.0   0.0   0.0
2        0        0   0.0   0.0   0.0
```
## 3. df.assign
assign을 활용하면 다음과 같이 columns 여러개를 추가할 수 있다.
```python
print(df)
>>>
   col1
0     0
1     0
2     0
>>>
col1  col2  col2
0   0.0   0.0   0.0
0   0.0   0.0   0.0
0   0.0   0.0   0.0
```
또한 함수나 lambda를 주어 열을 생성할 수 도 있다.

기존에 존재하던 열을 이용하여 다음과 같이 제곱근과 제곱값을 가진 열을 추가 할 수 있다.
```python
df.assign(new_col1=[1,2,3],new_col2=[2,3,4])

df.assign(mean_col= lambda x: x.col1**1/2, pow_col = lambda x :x.col1**2 )
print(df)
>>>
   col1  mean_col  pow_col
0     4       2.0       16
1     8       4.0       64
2     1       0.5        1
```
assign을 활용할 경우 중복되는 열은 새로 추가되지 않고 overwriting 됨에 주의해야 한다.
```python
df
>>>
   col1  col2
0     0     0
1     0     0
2     0     0

df.assign(col1=[0,0,0],col2=[0,0,0])
>>>
   col1  col2
0     0     0
1     0     0
2     0     0
```



