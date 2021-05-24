## map
기본적으로 간단하게 lamda를 활용 할 수 있다. 이때는 apply, transform method와 동일한 기능이다.
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



