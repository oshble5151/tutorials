## pandas 합치기
2개의 DataFrame을 합쳐보고자 한다.

다음과 같이 2개의 DataFrame이 있다.
```python
print(df1)
>>>
   name    job
0  Jack   boss
1  Mary  woker
2  Cony   boss

print(df2)
>>>
   name    job
0  Poll  woker
1  Gwen  woker
2  Jack   boss
```

## concaternate - columns name이 같은 경우 
 columns name이 같은 경우 concaternate로 간단하게 data를 합칠 수 있다.
 ```python
 df_new = pd.concat([df1,df2])
 >>>
   name    job
0  Jack   boss
1  Mary  woker
2  Cony   boss
0  Poll  woker
1  Gwen  woker
2  Jack   boss 
```
잘 합쳐졌지만 index가 0,1,2,0,1,2로 중복되었다.

이는 ignore_index 인수를 활용하여 수정 가능하다.
```
df_new = pd.concat([df2,df3], ignore_index =1)
>>>
   name    job
0  Jack   boss
1  Mary  woker
2  Cony   boss
3  Poll  woker
4  Gwen  woker
5  Jack   boss
```
append method로 동일하게 합쳐줄 수 있다.
```
df2.append(df3,ignore_index=1)
>>>
   name    job
0  Jack   boss
1  Mary  woker
2  Cony   boss
3  Poll  woker
4  Gwen  woker
5  Jack   boss
```

다음과 같이 axis 인수로 행 기준으로 합치는 것도 가능하다.
```python
print(df4)
>>>
   age country
0   30   Korea
1   22   Japan
2   35     U.S

pd.concat([df2,df4],axis=1)
>>> 
   name    job   age  country
0  Jack   boss    30    Korea
1  Mary  woker    22    Japan
2  Cony   boss    35      U.S
```
