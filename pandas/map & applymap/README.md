## map
기본적으로 간단하게 lamda를 활용 할 수 있다. 이때는 apply, transform method와 동일한 기능이다.

map은 pd.Series의 method이며 pd.DataFrame에서는 사용할 수 없다.
```python
print(df)
>>>
   name blood_type   grade
0  Jack          A  normal
1   Any          O    good
2  Pola         AB     bad
3  Mack          B  normal
```
만약 grade가 good이면 70, normal이면 50, bad면 30점을 부여하고자 한다.
```python
def new_score(grade):
  score = [30,50,70]
  if grade == 'normal':
    return score[1]
  elif  grade == 'good':
    return score[2]
  else:
    return score[0]

df['score'] = df.grade.map(new_score)

print(df)
>>>
   name blood_type   grade  score
0  Jack          A  normal     50
1   Any          O    good     70
2  Pola         AB     bad     30
3  Mack          B  normal     50
```
map method에 ditionary를 활용하여 값을 mapping 시켜줄 수 있다.
```python
df.blood_type = df.blood_type.map({'A':'B','O':'O','AB':'AB','B':'A'})
>>>
0     B
1     O
2    AB
3     A
Name: blood_type, dtype: object

```
지정 되지 않은 값이 있으면 None으로 처리된다.
```python
df.blood_type = df.blood_type.map({'A':'B','B':'A'})
>>>
   name blood_type   grade  score
0  Jack          B  normal     50
1   Any        NaN    good     70
2  Pola        NaN     bad     30
3  Mack          A  normal     50
```

## applymap
applymap은 특정값을 DataFrame 전체에 추가하거나 적용 시켜 주고 싶을때 사용한다.
```python
print(df)
>>>
   x  y  z
0  7  2  0
1  0  1  3
2  5 -4  0

df.applymap(lambda x: x+0.5)
>>>
     x    y    z
0  7.5  2.5  0.5
1  0.5  1.5  3.5
2  5.5 -3.5  0.5
```
