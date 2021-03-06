## merge
pandas는 간단하게 합칠수 있는 concat, append 외에도 merge를 이용하여 자료를 합칠 수 있다.
```python
print(df1)
>>>
  class subject
0     A    Math
1     B     Eng
2     C     Eng
3     D    Math
print(df2)
>>>
  class subject
0     B     Eng
1     B    Math
2     A     Eng
3     C    Math
```
merge는 how 인수의 defalut값이 'inner'이다. inner은 교집합을 의미한다.

가장 기본적으로 merge하면 다음과 같다.
```python
df1.merge(df2)
>>>
  class subject
0     B     Eng
```
두 열의 값이 동일한 data만 출력되었음을 알 수 있다.

how='outer'로 합칠 경우 concat의 결과와 같다.
```python
df1.merge(df2,'outer')
>>>
  class subject
0     A    Math
1     B     Eng
2     C     Eng
3     D    Math
4     B    Math
5     A     Eng
6     C    Math
```

on 인수를 통해, 한 열을 기준으로 다른 열이 어떻게 속해 있는지를 확인 할 수 있다.

어떤 class에 어떤 과목이 속해 있는지를 다음과 같이 확인 할 수 있다.
```python
df1.merge(df2,on=['class'])
>>>
  class subject_x subject_y
0     A      Math       Eng
1     B       Eng   History
2     C       Eng      Math
3     D      Math       P.E
```
마찬가지로 어떤 subject가 어떤 class에서 실행되는지 알기 위해서 다음과 같이 확인해 볼수 있다.
```python
df1.merge(df2,on=['subject'])
>>>
  class_x subject class_y
0       A    Math       C
1       D    Math       C
2       B     Eng       A
3       C     Eng       A
```
