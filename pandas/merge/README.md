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
