## reindex
pandas는 reindex를 통해 index의 순서를 바꿀 수 있다.
```python
print(df)
>>>
          Jack    Tom   Keny
tall     173.0  174.0  172.0
weigth    60.0   70.0   65.0
sight      1.5    2.0    1.0

df.reindex(['weigth','sight','tall'])
>>>
         Jack    Tom   Keny
weigth   60.0   70.0   65.0
sight     1.5    2.0    1.0
tall    173.0  174.0  172.0
```

다음과 같이 열의 순서도 변경 가능하다.
```python
df.reindex(['Tom','Keny','Jack'],axis=1)
# or, df.reindex(columns=['Tom','Keny','Jack'])
>>>
          Tom   Keny   Jack
tall    174.0  172.0  173.0
weigth   70.0   65.0   60.0
sight     2.0    1.0    1.5
```
## index 확장 및 값 지정 
reindex로 순서변경 뿐만 아니라 확장도 가능하다. 이때 기존에 없던 index를 추가하면 None값이 들어간다.

다음과 같이 Michael의 정보를 추가할 수 있다.

```python
df.reindex(list(df.columns)+['Michael'],axis=1)
>>>
          Tom   Keny   Jack  Michael
tall    174.0  172.0  173.0      NaN
weigth   70.0   65.0   60.0      NaN  
sight     2.0    1.0    1.5      NaN
```
NaN값으로 채우고 싶지 않은 경우, fill_value를 통해 확장시 들어갈 값을 지정할 수 있다.
```python
df.reindex(list(df.columns)+['Michael'],axis=1, fill_value = 'Unknown')
>>>
          Tom   Keny   Jack  Michael
tall    173.0  174.0  172.0  Unknown
weight   60.0   70.0   65.0  Unknown
sight     1.5    2.0    1.0  Unknown
```
Michael의 모든 신체 정보가 Jack과 같을 수가 있다. 

이 경우 다음과 같이 method 인수를 활용하면, Jack과 같은 값을 확장과 동시에 지정해줄 수 있다.
```python
df_org_columns = list(df.columns)
df.columns = [0,1,2]
df = df.reindex([0,1,2,3],axis =1,method='ffill')
print(df)
>>>
            0      1      2      3
tall    173.0  174.0  172.0  172.0
weight   60.0   70.0   65.0   65.0
sight     1.5    2.0    1.0    1.0

df.columns = df_org_columns + ['Michael']
>>>
          Tom     Keny    Jack  Michael
tall    173.0    174.0   172.0    172.0
weight   60.0     70.0    65.0     65.0 
sight     1.5      2.0     1.0      1.0
```
method 인수를 사용하려면 index(혹은 columns)이 오름차, 혹은 내림차순 이어야 한다.

그렇지 않으면 index must be monotonic increasing or decreasing 오류가 발생함에 주의해야 한다.





